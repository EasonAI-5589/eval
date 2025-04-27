import os
import json
import argparse



def eval_pope(answers, label_file):
    label_list = [json.loads(q)['label'] for q in open(label_file, 'r')]

    for answer in answers:
        text = answer['text']

        # Only keep the first sentence
        if text.find('.') != -1:
            text = text.split('.')[0]

        text = text.replace(',', '')
        words = text.split(' ')
        if 'No' in words or 'not' in words or 'no' in words:
            answer['text'] = 'no'
        else:
            answer['text'] = 'yes'

    for i in range(len(label_list)):
        if label_list[i] == 'no':
            label_list[i] = 0
        else:
            label_list[i] = 1

    pred_list = []
    for answer in answers:
        if answer['text'] == 'no':
            pred_list.append(0)
        else:
            pred_list.append(1)

    pos = 1
    neg = 0
    yes_ratio = pred_list.count(1) / len(pred_list)

    TP, TN, FP, FN = 0, 0, 0, 0
    for pred, label in zip(pred_list, label_list):
        if pred == pos and label == pos:
            TP += 1
        elif pred == pos and label == neg:
            FP += 1
        elif pred == neg and label == neg:
            TN += 1
        elif pred == neg and label == pos:
            FN += 1

    print('TP\tFP\tTN\tFN\t')
    print('{}\t{}\t{}\t{}'.format(TP, FP, TN, FN))

    precision = float(TP) / float(TP + FP)
    recall = float(TP) / float(TP + FN)
    f1 = 2*precision*recall / (precision + recall)
    acc = (TP + TN) / (TP + TN + FP + FN)
    print('Accuracy: {}'.format(acc))
    print('Precision: {}'.format(precision))
    print('Recall: {}'.format(recall))
    print('F1 score: {}'.format(f1))
    print('Yes ratio: {}'.format(yes_ratio))
    print('%.3f, %.3f, %.3f, %.3f, %.3f' % (f1, acc, precision, recall, yes_ratio) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotation-dir", default="/root/autodl-tmp/LLaVA/playground/data/eval/pope/coco",type=str)
    parser.add_argument("--question-file", default="/root/autodl-tmp/LLaVA/playground/data/eval/pope/test.jsonl",type=str)
    parser.add_argument("--result-file", default="/root/autodl-tmp/LLaVA/playground/data/eval/pope/answers/llava-v1.5-7b.jsonl",type=str)
    args = parser.parse_args()

    # 读取所有question和llava answers
    questions_list = [json.loads(line) for line in open(args.question_file)]
    answers = [json.loads(q) for q in open(args.result_file)]

    # 对于question来说
    # 1到3000行是adversarial
    # 3001到6000行是popular
    # 6001到9000行是random
    adversarial_questions = questions_list[:3000]
    popular_questions = questions_list[3000:6000]
    random_questions = questions_list[6000:]

    # 对于answer来说同理
    # 1到3000行是adversarial
    # 3001到6000行是popular
    # 6001到9000行是random

    adversarial_answers = answers[:3000]
    popular_answers = answers[3000:6000]
    random_answers = answers[6000:]

    # 评估adversarial_answers
    print("====================================")
    print("Category: adversarial, # samples: {}".format(len(adversarial_answers)))
    eval_pope(adversarial_answers, os.path.join(args.annotation_dir, 'coco_pope_adversarial.jsonl'))

    # 评估popular_answers
    print("====================================")
    print("Category: popular, # samples: {}".format(len(popular_answers)))
    eval_pope(popular_answers, os.path.join(args.annotation_dir, 'coco_pope_popular.jsonl'))

    # 评估random_answers
    print("====================================")
    print("Category: random, # samples: {}".format(len(random_answers)))
    
    eval_pope(random_answers, os.path.join(args.annotation_dir, 'coco_pope_random.jsonl'))
