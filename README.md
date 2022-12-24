# Menhera-Diary-Resource

Resource files of com.tencent.tmgp.menhera （《胡桃日记》）

The game is published by [Tencent](https://htrj.qq.com/) and will be shut down in February 2023.

Game developers should be shameful for shutting their online games down without releasing offline versions.

## Folders

* `assets` - Assets files from game APK
* `StreamingRes` - recent hot update files

There's no extracted files in this repository. The extracted files are large and will waste disk space. Just do it by yourself if you need.

## AssetBundle files

Most of the game resources are standard Unity AssetBundle files. [AssetStudio](https://github.com/Perfare/AssetStudio) should just works.

## wem and bnk files

[Wwise-Unpacker](https://github.com/mortalis13/Wwise-Unpacker) is used to unpack bnk files.

Execute `ww2ogg *.wem --pcb packed_codebooks_aoTuV_603.bin` to convert wem files to ogg, and use `ffmpeg` to convert ogg to wav (may fix wrong length playing problem).

## Disclaimer

This project is for educational purposes only. I do not own the game and I do not intend to distribute it.

The game resource files are archived here for public interest reasons.
