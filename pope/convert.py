import json
import os

def generate_llava_pope_test_jsonl(annotation_dir, output_file):
    files = {
        "adversarial": "coco_pope_adversarial.jsonl",
        "popular": "coco_pope_popular.jsonl",
        "random": "coco_pope_random.jsonl"
    }

    with open(output_file, "w") as out_f:
        for category, filename in files.items():
            file_path = os.path.join(annotation_dir, filename)
            with open(file_path, "r") as f:
                for line in f:
                    if line.strip():  # 忽略空行
                        item = json.loads(line)
                        entry = {
                            "question_id": item["question_id"],
                            "image": item["image"],
                            "text": item["text"].strip(), # 删除"\nAnswer the question using a single word or phrase."
                            "category": category
                        }
                        out_f.write(json.dumps(entry) + "\n")


if __name__ == "__main__":

     # 获取当前脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构造相对路径
    annotation_dir = os.path.join(script_dir, "coco")
    output_file = os.path.join(script_dir, "llava_test_wo_Answer the question.jsonl")

    generate_llava_pope_test_jsonl(
        annotation_dir= annotation_dir,
        output_file= output_file
    )

