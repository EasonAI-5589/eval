# 下载数据集

## 下载 VizWiz 数据

### 下载测试图片
使用以下命令下载测试图片的压缩包 `test.zip`，并将下载日志保存到 `vizwiz.log` 文件中：
```bash
nohup wget https://vizwiz.cs.colorado.edu/VizWiz_final/images/test.zip > vizwiz.log 2>&1 &
```

### 下载标注文件
使用以下命令下载标注文件的压缩包 `Annotations.zip`：
```bash
wget https://vizwiz.cs.colorado.edu/VizWiz_final/vqa_data/Annotations.zip
```

### 移动文件到目标目录
将下载的 `test.zip` 和 `Annotations.zip` 移动到目标目录 `./playground/data/eval/vizwiz`：
```bash
mv test.zip ./playground/data/eval/vizwiz
mv Annotations ./playground/data/eval/vizwiz/
```

### 解压文件
进入目标目录并解压 `test.zip`，然后删除压缩包：
```bash
cd ./playground/data/eval/vizwiz
unzip test.zip
rm test.zip
```

解压 `Annotations.zip`，然后删除压缩包：
```bash
unzip Annotations.zip
rm Annotations.zip
```