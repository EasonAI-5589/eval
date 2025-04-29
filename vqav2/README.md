# 下载数据集

## 下载 VQAV2 数据
```bash
nohup wget http://images.cocodataset.org/zips/test2015.zip > vqav2.log 2>&1 &
```

解压

unzip test2015.zip -d ./playground/data/eval/vqav2

rm test2015.zip

# 修改脚本