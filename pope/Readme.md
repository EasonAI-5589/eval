# 跑POPE数据集

## 本文件夹包含的内容

下载完成的coco文件夹，包含三个ground truth文件
\coco\coco_pope_random.json
\coco\coco_pope_popular.json
\coco\coco_pope_adversarial.json

最好把这三个文件转化为jsonl，但是scripts的问题，不需要管，就用json文件就可以了

# 使用镜像源下载
wget http://images.cocodataset.org/zips/val2014.zip

# 解压
unzip val2014.zip -d /root/autodl-tmp/val2014