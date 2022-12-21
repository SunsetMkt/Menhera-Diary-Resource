# Get latest game apk resource
import zipfile

import lxml.html
import requests
import tqdm

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_download_url():
    page_url = "https://htrj.qq.com/zlkdatasys/mct/d/play.shtml?device=android"
    # Get all script src
    response = requests.get(page_url, headers=headers)
    html = lxml.html.fromstring(response.text)
    script_src = html.xpath('//script/@src')
    # Get the src contains myapp.com
    for src in script_src:
        if 'myapp.com' in src:
            download_url_js = src
            break
    print(download_url_js)
    # if url begin with // add https:
    if download_url_js.startswith('//'):
        download_url_js = 'https:' + download_url_js
    # Get the download url
    response = requests.get(download_url_js, headers=headers)
    print(response.text)
    # androidURL: 'https://dlied4.myapp.com/myapp/1107876280/cos.release-75289/10040714_com.tencent.tmgp.menhera_a2051185_1.6.7.0_lz3uhY.apk',
    download_url = response.text.split('androidURL:')[1].split(',')[
        0].strip().strip("'")
    return download_url


def download_file(url, file_name):
    # Show progress bar
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(block_size):
                t.update(len(chunk))
                f.write(chunk)
        t.close()


def get_filename(url):
    return url.split('/')[-1]


def unzip_assets(file_name):
    # unzip assets folder, begin with assets/
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.startswith('assets/'):
                zip_ref.extract(file)


def update_gitignore(filename):
    with open('.gitignore', 'a') as f:
        f.write(filename + '\n')


def in_gitignore(filename):
    with open('.gitignore', 'r') as f:
        for line in f:
            if line.strip() == filename:
                return True
    return False


def save_curr_apk_name(filename):
    with open('curr_apk_name.txt', 'w') as f:
        f.write(filename)


if __name__ == '__main__':
    download_url = get_download_url()
    file_name = get_filename(download_url)
    if not in_gitignore(file_name):
        download_file(download_url, file_name)
        unzip_assets(file_name)
        update_gitignore(file_name)
        save_curr_apk_name(file_name)
    else:
        raise Exception(file_name + ' already processed.')
