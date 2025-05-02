# 下载数据集

## 下载 TextVQA 数据

### 下载测试图片
使用以下命令下载测试图片的压缩包 `train_val_images.zip`，并将下载日志保存到 `textvqa_images.log` 文件中：
```bash
nohup wget https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip > textvqa_images.log 2>&1 &
```

### 下载标注文件
https://dl.fbaipublicfiles.com/textvqa/data/TextVQA_0.5.1_val.json

使用以下命令下载标注文件`TextVQA_0.5.1_val.json`：
```bash
nohup wget https://dl.fbaipublicfiles.com/textvqa/data/TextVQA_0.5.1_val.json > textvqa_annotations.log 2>&1 &
```

### 移动文件到目标目录

```bash
mv train_val_images.zip /root/autodl-tmp/eval/textvqa
mv TextVQA_0.5.1_val.json /root/autodl-tmp/eval/textvqa
```

### 解压文件
进入目标目录并解压 `train_val_images.zip`，然后删除压缩包：
```bash
cd /root/autodl-tmp/eval/textvqa
unzip train_val_images.zip
rm train_val_images.zip
```



