# 下载数据集

## 下载 GQA 数据
```bash
nohup wget https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip > gqa-images.log 2>&1 &
```

## 下载 GQA 评估脚本
```bash
nohup wget https://nlp.stanford.edu/data/gqa/eval.zip > gqa-eval.log 2>&1 &
```

## 一键下载脚本
```bash
nohup wget https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip > gqa-images.log 2>&1 &
nohup wget https://nlp.stanford.edu/data/gqa/eval.zip > gqa-eval.log 2>&1 &
```

## 查看下载日志
```bash
cat /root/autodl-tmp/LLaVA/gqa-eval.log
cat /root/autodl-tmp/LLaVA/gqa-images.log
```

## 解压并移动到目标路径
目标路径：`./playground/data/eval/gqa/data`

```bash
unzip images.zip -d ./playground/data/eval/gqa/data/
unzip eval.zip -d ./playground/data/eval/gqa/data/
```

## 删除 ZIP 文件
确保磁盘有足够的容量，并确认上述步骤已完成后删除 ZIP 文件：
```bash
rm images.zip
rm eval.zip
```


## 跨文件夹移动eval/gqa
cp -r /root/autodl-tmp/DoubleAttentionVLM/playground/data/eval/gqa/data /root/autodl-tmp/FasterVLM/playground/data/eval/gqa


## 修改eval.py

将
/root/autodl-tmp/FasterVLM/playground/data/eval/gqa/data/eval.py
替换成
\eval\gqa\eval.py