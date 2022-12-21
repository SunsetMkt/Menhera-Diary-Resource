# Menhera-Diary-Reverse

Reverse engineering of com.tencent.tmgp.menhera

With the help of [DevXUnityUnpacker](https://github.com/Polarmods/DevX-Cracked).

The game is published by [Tencent](https://htrj.qq.com/).

## Folders

* StreamingRes - Contains recent hot fix files
* Project - Pseudo-Unity-Project created by DevXUnityUnpacker from APK

## Disclaimer

This project is for educational purposes only. I do not own the game and I do not intend to distribute it.

## Tips

### Recursively create .gitkeep files

```bash
find . -type d -empty -not -path "./.git/*" -exec touch {}/.gitkeep \;
```

[Source](http://cavaliercoder.com/blog/recursively-create-gitkeep-files.html)
