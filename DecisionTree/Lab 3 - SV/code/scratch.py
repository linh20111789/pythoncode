# %%
"""
# Lab 3: Classification

**Bài tập rèn luyện khả năng cài đặt thuật toán Decision tree.**

Cập nhật lần cuối: 28/02/2021 

Họ tên: 

MSSV: 
"""

# %%
"""
## Quy định cách làm bài và nộp bài
"""

# %%
"""
&#127827; *Trong bài tập này, các bạn chỉ được phép sử dụng các thư viện Standard Python Library, numpy, pandas, matplotlib. Các thư viện hỗ trơ (đặc biệt là thư viện Sklearn) là không được phép. Thư viện Sklearn chỉ được dùng trong phần huấn luyện mô hình cây quyết định (mình sẽ nói rõ ở phần đó)*

&#127802; Sinh viên lưu ý mình sẽ dùng chương trình hỗ trợ chấm bài nên bạn cần phải tuân thủ chính xác qui định mà mình đặt ra, nếu không rõ thì hỏi, chứ không nên tự tiện làm theo ý của cá nhân.

**Cách làm bài**

Bạn sẽ làm trực tiếp trên file Python notebook này. Đầu tiên, bạn điền họ tên và MSSV vào phần đầu file ở bên trên. Trong file, bạn làm bài ở những chỗ có ghi là:

```python
# YOUR CODE HERE
raise NotImplementedError()
```
hoặc đối với những phần code không bắt buộc thì là:
```python
# YOUR CODE HERE (OPTION)
```

Tất nhiên, khi làm thì bạn xóa dòng `raise NotImplementedError()` đi.
Đối những phần yêu cầu code thì thường ở ngay phía dưới sẽ có một (hoặc một số) cell chứa các bộ test để giúp bạn biết đã code đúng hay chưa; nếu chạy cell này không có lỗi gì thì có nghĩa là qua được các bộ test. Trong một số trường hợp, các bộ test có thể sẽ không đầy đủ; nghĩa là, nếu không qua được test thì là code sai, nhưng nếu qua được test thì chưa chắc đã đúng hoàn toàn.

Trong khi làm bài, bạn có thể cho in ra màn hình, tạo thêm các cell để test. Nhưng khi nộp bài thì bạn xóa các cell mà bạn tự tạo, xóa hoặc comment các câu lệnh in ra màn hình. Bạn lưu ý <font color=red>không được tự tiện xóa các cell hay sửa code của Thầy</font> (trừ những chỗ được phép sửa như đã nói ở trên).


Trong khi làm bài, thường xuyên `Ctrl + S` để lưu lại bài làm của bạn, tránh mất mát thông tin.

Bạn có thể thảo luận ý tưởng với bạn khác hoặc từ các nguồn khác, nhưng code và bài làm phải là của bạn, dựa trên sự hiểu thật sự của bạn. Nếu vi phạm thì sẽ bị 0 điểm cho toàn bộ môn học.

**Cách nộp bài**

Khi chấm bài, đầu tiên mình sẽ chọn `Kernel` - `Restart & Run All` để restart và chạy tất cả các cell trong notebook của bạn; do đó, trước khi nộp bài, bạn nên chạy thử `Kernel` - `Restart & Run All` để đảm bảo mọi chuyện diễn ra đúng như mong đợi.

Sau đó, bạn tạo thư mục nộp bài theo cấu trúc sau:
- Thư mục `MSSV` (vd, nếu bạn có MSSV là 123 thì bạn đặt tên thư mục là `123`)
    - File `Lab3 - cratch.ipynb` 
    - File `Lab3 - mnist.ipynb` 
- Các bạn nén lại MSSV.zip (*.zip chứ không phải .rar hay gì khác)

Cuối cùng, bạn nén thư mục `MSSV` này lại và nộp ở link trên moodle. <font color=red>Bạn lưu ý tuân thủ chính xác qui định nộp bài.</font>
"""

# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# YOUR CODE HERE (OPTION) 
# Mình nhắc lại, không được dùng các thư viện hỗ trợ cài đặt thuật toán, ví dụ: Sklearn, Keras,...

# %%
"""
# Giới thiệu về dữ liệu

- Trong bài tập này, mình sẽ tạo một bộ dữ liệu nhỏ để minh họa quá trình cài đặt thuật toán cây quyết định. 
- Bộ dữ liệu gồm các thuộc tính: màu sắc, trọng lượng, loại trái cây. Nhiệm vụ của chúng ta là dựa vào màu sắc và trọng lượng, dự đoán loại trái cây.
- Dữ liệu được cho trong biến **training_data**. Dữ liệu gồm 5 dòng và 3 cột, trong đó: 
    + 5 dòng tương ứng với 5 điểm dữ liệu.
    + 3 cột, 2 cột đầu tiên tương ứng là màu sắc (color) và trọng lượng (weight), cột cuối cùng tương ứng là loại trái cây (label).
"""

# %%
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

# %%
"""
# Cài đặt thuật toán Decision tree
"""

# %%
"""
## Gini Index

*Để hiểu rõ hơn về về phần Gini Index, bạn có thể đọc phần Gini Index, phần 8.2 sách Data Mining Concepts and Techniques.*

- Độ đo Gini Index tính toán sự Impurity của tập dữ liệu cụ thể.
- Độ đo Gini nằm trong khoảng [0, 1]. Với giá trị Impurity thấp nghĩa là dữ liệu ít hỗn loạn, ngược lại Impurity cao nghĩa là dữ liệu lộn xộn.

- Tóm lại, bạn có thể tính độ đo Gini của tập dữ liệu D bằng công thức


$$
Gini(D) = 1 - \sum \limits_{i=1}^{m} {p_i}^2 
$$

Với: <br />
m: số lượng lớp. <br />
$p_i$: là tỷ lệ số điểm dữ liệu được gắn nhãn là i.

- Nhiệm vụ của sinh viên: hoàn thành hàm *gini* bên dưới.
-  Gợi ý, sinh viên có thể sử dụng hàm *class_counts* đã được cung cấp bên dưới. Bên dưới hàm *class_counts* có ví dụ, để mô tả cách dùng của hàm.
"""

# %%
def class_counts(data):
    """
    Counts the number of each type of example in a dataset.    
    """
    counts = {}  # a dictionary of label -> count.
    for row in data:
        # in our dataset format, the label is always the last column
                
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

# Example of class_counts function
cnt = class_counts(training_data)
print("cnt = ",cnt)

# %%
def gini(training_data):
    """
    Calculate the Gini Impurity for a list of labels
    """
    impurity = None
    
    # YOUR CODE HERE
    raise NotImplementedError()    
    
    return impurity

# %%
# TEST
labels = [['Orange'], ['Orange']]
assert gini(labels) == 0.0

labels = [['Orange'], ['Lemon']]
assert gini(labels) == 0.5

# %%
"""
- Độ đo Gini xem xét việc phân chia nhị phân của thuộc tính. 
- Khi xem xét phân tách nhị phân, ta tính tổng có trọng số impurity của mỗi phân vùng trái và phải. Ví dụ, nếu phân tách A, tách tập dữ liệu D thành D1 và D2, thì Gini Index của D theo phân tách A là: 
$$
Gini_A (D) = \frac{|D_1|}{|D|} Gini(D_1) + \frac{|D_2|}{|D|} Gini(D_2)
$$

- Độ giảm impurity (reduction in impurity) được tính theo công thức:
$$
\Delta Gini(A) = Gini(D) - Gini_A(D)       
$$ 
<br />

- Nhiệm vụ của sinh viên: hoàn thành hàm *reduction_gini_impurity* bên dưới (theo công thức $\Delta Gini(A)$).
"""

# %%
def reduction_gini_impurity(left_partition, right_partition, current_gini):
    """
    Calculate the reduction in impurity
    
    * Parameter:
    - left_partition: a python list, indicate D1 partition in the previous equation
    - right_partition: a python list, indicate D2 partition in the previous equation
    - current_gini: a number, indicate Gini(D) in the previous equation
    
    * Return:
    - reduction_impurity: a float number
    """
    
    reduction_impurity = None
    
    # YOUR CODE HERE
    raise NotImplementedError()
    
    return reduction_impurity

# %%
# TEST

left_partion = [['Green', 3, 'Apple']]
right_partion = [['Yellow', 3, 'Apple'],
                 ['Red', 1, 'Grape'],
                 ['Red', 1, 'Grape'],
                 ['Yellow', 3, 'Lemon']]

current_gini = gini(training_data)

assert reduction_gini_impurity(left_partion, right_partion, current_gini) == 0.1399999999999999

# %%
"""
## Split a dataset (Phân tách dữ liệu dựa vào Gini Index)

- Với độ đo Gini bên trên, ta kiểm tra mọi giá trị trên mỗi thuộc tính. Thuộc tính có reduction in impurity lớn nhất, sẽ được chọn làm phân tách.
_________

- Đầu tiên, sinh viên code hàm *partition* bên dưới. Hàm partition có nhiệm vụ phân chia dữ liệu, dựa vào thuộc tính đang xét, có giá trị như thế nào so với điểm phân chia (value of split-point).

- Đối với dữ liệu numerical, hàm *partition* kiểm tra xem tại mỗi điểm dữ liệu (mỗi dòng), thuộc tính column có giá trị như thế nào với value. 
    + Nếu giá trị tại cột column của dòng i **lớn hơn hoặc bằng** value thì thêm dòng i vào left_partition. 
    + Ngược lại thêm dòng i vào right_partition.
    
- Đối với dữ liệu categorical:
    + Nếu giá trị tại cột column của dòng i **bằng** value thì thêm dòng i vào left_partition. 
    + Ngược lại thêm dòng i vào right_partition.
"""

# %%
def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

# %%
def partition(training_dataset, column, value):
    """
    Partitions a dataset. 
    
    * Parameters:
    - training_dataset
    - column: a number, indicate current column
    - value: a number or string, indicate a split-point value
    
    * Returns:
    - left_partition: a python list
    - right_partition: a python list
    """
    
    left_partition, right_partition = [], []
    
    # YOUR CODE HERE
    raise NotImplementedError()
    
    return left_partition, right_partition

# %%
# TEST 

left_partition, right_partition = partition(training_data, 0, value='Red')
assert left_partition == [['Red', 1, 'Grape'], ['Red', 1, 'Grape']]
assert right_partition == [['Green', 3, 'Apple'], ['Yellow', 3, 'Apple'], ['Yellow', 3, 'Lemon']]

# %%
"""
- Cuối cùng, sinh viên sẽ hoàn thành hàm *find_best_split*
"""

# %%
def find_best_split(dataset):
    """
    Find the best split point by calculate reduction in impurity
    
    * Parameters:
    - dataset: a 2D python list
    
    * Return: 
    - best_reduction_impurity: a float number, indicate the maximum reduction in impurity
    - best_col: an int number, indicate column of split-point
    - best_val: a number or string, indicate value of split-point
    """
    
    best_reduction_impurity = 0  # keep track of the best information gain    
    current_uncertainty = gini(dataset) 
    best_col = None
    best_val = None
    n_features = len(dataset[0]) - 1  # number of columns

    for col in range(n_features):  # for each feature

        values = set([row[col] for row in dataset])  # unique values in the column

        for val in values:  # for each value

            current_col = col
            current_val = val

            # try splitting the dataset
            left_partition, right_partition = partition(dataset, current_col, current_val)

            # Skip this split if it doesn't divide the dataset.
            if len(left_partition) == 0 or len(right_partition) == 0:
                continue

            # Calculate the reduction impurity from left_partition and right_partition 
            # (CALL reduction_gini_impurity FUNCTION)
            
            # YOUR CODE HERE
            raise NotImplementedError()
            
            # UPDATE best_reduction_impurity, best_col, best_val
            if reduction_impurity >= best_reduction_impurity:
                # YOUR CODE HERE
                raise NotImplementedError()

    return best_reduction_impurity, best_col, best_val

# %%
# TEST
reduction_impurity, col, val = find_best_split(training_data)
assert col == 1
assert val == 3

# %%
"""
# Huấn luyện
"""

# %%
"""
- Đầu tiên là nút lá (node leaf/ ternimal node), có nhiệm vụ dự đoán. 
- Nút lá sẽ trả về python dictionary, với định dạng {lớp: số lần xuất hiện}
- Ví dụ: 
```python
{'Apple': 1, 'Lemon': 1}
```
"""

# %%
class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the dataset from the training data that reach this leaf.
    """

    def __init__(self, dataset):
        self.predictions = class_counts(dataset)

# %%
"""
- Tiếp theo là Decision node (nút quyết định), có nhiệm vụ phân chia dữ liệu, gồm các thuộc tính: 
    + col: thuộc tính nào đang được xét
    + val: giá trị split-point là bao nhiêu
    + left_branch: nhánh bên trái (trường hợp giá trị >= split-point)
    + right_branch: nhánh bên phải (trường hợp giá trị < split-point)
"""

# %%
class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 col,
                 val,
                 left_branch,
                 right_branch):
        self.col = col
        self.val = val
        self.left_branch = left_branch
        self.right_branch = right_branch

# %%
"""
- Hàm xây dựng cây *build_tree* được xây dựng bên dưới. Mình đã hỗ trợ các bạn phần này.
"""

# %%
def build_tree(dataset):
    """
    Builds the tree.
    """

    # Find best split-point
    reduction_impurity, col, val = find_best_split(dataset)

    # Base case
    if reduction_impurity == 0:
        return Leaf(dataset)

    # If we reach here, we have found a useful feature / value to partition.
    left_partition, right_partition = partition(dataset, col, val)

    # Recursively build the left branch.
    left_branch = build_tree(left_partition)

    # Recursively build the right branch.
    right_branch = build_tree(right_partition)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(col, val, left_branch, right_branch)

# %%
"""
- Đến đây chúng ta đã sẵn sàng để huấn luyện mô hình Cây quyết định (Decision tree). Cây quyết định được lưu vào biến **my_tree**
"""

# %%
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

my_tree = build_tree(training_data)

# %%
"""
# Phân lớp (Classify)

- Ta tiến hành phân lớp dựa vào cây quyết định vừa được huấn luyện. Bằng cách sử dụng hàm classify được cung cấp sẵn bên dưới.
"""

# %%
def classify(new_data, node):

    # Base case - a leaf node
    if isinstance(node, Leaf):
        return node.predictions

    # Classify depend on the property of decistion tree
    
    if is_numeric(node.val):        
        if new_data[node.col] >= node.val:    
            return classify(new_data, node.left_branch)
        else:
            return classify(new_data, node.right_branch)

    else: 
        if new_data[node.col] == node.val:
            return classify(new_data, node.left_branch)
        else:
            return classify(new_data, node.right_branch)

# %%
new_data = ['Yellow', 3, 'Apple']

classify(new_data, my_tree)

# %%
"""
- Việc hiển thị, số lượng của mỗi lớp có vẻ không hay lắm. Ta sẽ dùng hàm *print_leaf* để chuyển về dạng %, nhìn sẽ chuyên nghiệp hơn.
"""

# %%
def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

# %%
print_leaf(classify(new_data, my_tree))

# %%
"""
# Print tree
"""

# %%
"""
- Sau khi đã huấn luyện cây quyết định, ta cần in cây quyết định ra màn hình. Mình sẽ giúp các bạn phần này.
"""

# %%
column_names = ['color', 'weight', 'labels']

def question(column, value):
    condition = "=="
    if is_numeric(value):
        condition = ">="
    return "Is %s %s %s?" % (column_names[column], condition, str(value))

# %%
def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + str(question(node.col, node.val)))

    # Call this function recursively on the left branch
    print (spacing + '--> left branch:')
    print_tree(node.left_branch, spacing + "  ")

    # Call this function recursively on the right branch
    print (spacing + '--> right branch:')
    print_tree(node.right_branch, spacing + "  ")

# %%
print_tree(my_tree)

# %%
"""
# Kiểm tra độ chính xác

- Sau khi đã huấn luyện thành công mô hình Cây quyết định, chúng ta sẽ kiểm tra độ chính xác của mô hình trên tập dữ liệu kiểm tra (testing dataset).

- Nhiệm vụ của các bạn, sẽ dự đoán trên tập dữ liệu **testing_data**. Kết quả sẽ được lưu vào biến **testing_data_pred**
"""

# %%
# Evaluate
testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

# %%
testing_data_pred = []

# YOUR CODE HERE
raise NotImplementedError()

# %%
# TEST 
assert testing_data_pred == [{'Apple': '100%'}, {'Apple': '50%', 'Lemon': '50%'}, \
                             {'Grape': '100%'}, {'Grape': '100%'}, {'Apple': '50%', 'Lemon': '50%'}]

# %%
