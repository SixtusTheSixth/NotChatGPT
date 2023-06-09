import csv
import tensorflow as tf

def get_data(train_path, test_path):
    train_abstracts = []
    train_labels = []
    test_abstracts = []
    test_labels = []
    total_skipped_pp_train = 0
    total_skipped_pp_test = 0
    total_added_pp_train = 0
    total_added_pp_test = 0
    with open(train_path) as train_csv:
        for line in csv.reader(train_csv):
            try:
                train_abstracts.append(line[0])
                train_labels.append(int(line[1]))
                total_added_pp_train += 1
            except:
                total_skipped_pp_train += 1
            
    with open(test_path) as test_csv:
        for line in csv.reader(test_csv):
            try:
                test_abstracts.append(line[0])
                test_labels.append(int(line[1]))
                total_added_pp_test += 1
            except:
                total_skipped_pp_test += 1

    print("total_skipped_pp_train", total_skipped_pp_train)
    print("total_added_pp_train", total_added_pp_train)
    print("total_skipped_pp_test", total_skipped_pp_test)
    print("total_added_pp_test", total_added_pp_test)

    train_abstracts = tf.convert_to_tensor(train_abstracts)
    train_labels = tf.convert_to_tensor(train_labels)
    train_labels = tf.one_hot(train_labels, 2)
    test_abstracts = tf.convert_to_tensor(test_abstracts)
    test_labels = tf.convert_to_tensor(test_labels)
    test_labels = tf.one_hot(test_labels, 2)
    return train_abstracts, train_labels, test_abstracts, test_labels

