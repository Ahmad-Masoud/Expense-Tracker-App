import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QDoubleSpinBox, QWidget, QLabel,QLineEdit, QGridLayout, QPushButton, QRadioButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle("Expense Tracker App")
window.setStyleSheet("background-color: #08083B;")
layout = QGridLayout()

for i in range(4):
    layout.setColumnStretch(i, 1)


def style_checkbox(checkbox):
    checkbox.setStyleSheet("""
    QCheckBox { color: white; font-size: 15px;}
    QCheckBox::indicator { width: 12px; height: 12px; border-radius: 4px; border: 2px solid white; background-color: white;}
    QCheckBox::indicator:checked { background-color: yellow; border: 2px solid yellow;}
    """)

def link_checkbox(checkbox, textbox):
    textbox.hide()

    def toggle():
        textbox.setVisible(checkbox.isChecked())

    checkbox.stateChanged.connect(toggle)

heading = QLabel("Expense Tracker App")
heading.setStyleSheet("color: white; font-size: 30px;")
heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

Name_label = QLabel("Name")
Name = QLineEdit()
Name.setPlaceholderText("Name")
Name.setStyleSheet("color: white;")
Name_label.setStyleSheet("color: white; font-size: 20px;")
Name.setFixedSize(500, 30)

Salary_Label = QLabel("Salary")
Salary = QDoubleSpinBox()
Salary.setRange(0, 99999999999)
Salary.setDecimals(4)
Salary.setFixedSize(500, 30)

def toggle_tax():
    Tax_Amount_box.setVisible(Tax_Amount.isChecked())
    Tax_Percent_box.setVisible(Tax_Percent.isChecked())

Tax_label = QLabel("Tax")
Tax_label.setStyleSheet("color: white; font-size: 20px;")

Tax_Amount = QRadioButton("Tax Amount")
Tax_Amount.setStyleSheet("""
QRadioButton::indicator{
    background-color: white;
    border-radius: 8px;
}
QRadioButton::indicator:checked{
    background-color: yellow;
}                                                  
                         """)
Tax_Amount_box = QDoubleSpinBox()
Tax_Amount_box.setStyleSheet("color: white;")
Tax_Amount_box.setFixedSize(500, 30)
Tax_Amount_box.setRange(0, 99999999999)
Tax_Amount_box.setDecimals(4)
Tax_Amount_box.hide()

Tax_Percent = QRadioButton("Tax Percentage")
Tax_Percent.setStyleSheet("""
QRadioButton::indicator{
    background-color: white;
    border-radius: 8px;
}
QRadioButton::indicator:checked{
    background-color: yellow;
}                                                  
                         """)

Tax_Percent_box = QDoubleSpinBox()
Tax_Percent_box.setStyleSheet("color: white;")
Tax_Percent_box.setFixedSize(500, 30)
Tax_Percent_box.setRange(0, 100)
Tax_Percent_box.setDecimals(4)
Tax_Percent_box.hide()

sub_text = QLabel("Expenditure")
sub_text.setStyleSheet("color: white; font-size: 20px;")

categories = ["Bills", "Food", "LifeStyle", "Vacations", "Debt"]

category_widgets = []

row = 11

def DataSave():
    name = Name.text()
    salary = Salary.value()

    if Tax_Amount.isChecked():
        tax = Tax_Amount_box.value()
        tax_type = "Amount"
    elif Tax_Percent.isChecked():
        tax = Tax_Percent_box.value()
        tax_type = "Percent"
    else:
        tax = 0
        tax_type = "None"

    expense_data = {}
    total_expense = 0

    for checkbox, textbox in category_widgets:
        if checkbox.isChecked():
            value = textbox.value()
            expense_data[checkbox.text()] = value
            total_expense += value
        else:
            expense_data[checkbox.text()] = 0


    data = {
        "Name" : name,
        "Salary" : salary,
        "Tax Type" : tax_type,
        "Tax Value" : tax,
        **expense_data
    }

    df = pd.DataFrame([data])

    file_name = f"{name}.csv"

    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a')
    else:
        df.to_csv(file_name)

    expense_data = get_expense_data()
    chart.plot_pie(expense_data)

for category in categories:
    checkbox =  QCheckBox(category)
    style_checkbox(checkbox)

    textbox = QDoubleSpinBox()
    textbox.setStyleSheet("color: white;")
    textbox.setFixedSize(500, 30)
    textbox.setRange(0, 999999999999)
    textbox.setDecimals(4)

    textbox.valueChanged.connect(DataSave)

    link_checkbox(checkbox, textbox)

    layout.addWidget(checkbox, row, 0)
    layout.addWidget(textbox, row + 1, 0)

    category_widgets.append((checkbox, textbox))

    row += 2

def create_graph(expense_data):

    categories = []
    values = []

    for category,value in expense_data.items():
        if value > 0:
            categories.append(category)
            values.append(value)

    plt.figure()
    plt.pie(values, labels=categories,autopct='1.1f%%',startangle=90)

    plt.title("Expense Distribution")

    plt.show()

class PieChartCanvas(FigureCanvas):
    def __init__(self):
        self.figure = Figure(facecolor="#08083B")
        super().__init__(self.figure)

    def plot_pie(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#08083B")

        categories = []
        values = []

        for category, value in data.items():
            if value > 0:
                categories.append(category)
                values.append(value)

        if values:
            ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90,textprops={'color': 'white'})
            ax.axis('equal')

        self.draw()
def get_expense_data():
    data = {}

    for checkbox, textbox in category_widgets:
        if checkbox.isChecked():
            data[checkbox.text()] = textbox.value()

    return data


button_1 = QPushButton("Save")
button_1.setStyleSheet("""
QPushButton {
    color:black;
    background-color: QLinearGradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff,
        stop:1 #d6d6d6
    );
    border: 2px solid #8f8f91;
    border-radius: 8px;
    padding: 6px;
}

QPushButton:pressed {
    background-color: #c0c0c0;
}
""")
button_1.setFixedSize(100, 40)
button_1.clicked.connect(DataSave)

Tax_Amount.toggled.connect(toggle_tax)
Tax_Percent.toggled.connect(toggle_tax)

layout.addWidget(heading, 0, 0, 1, 4)

chart = PieChartCanvas()
layout.addWidget(chart, 1, 2, 18, 2)

layout.addWidget(Name_label,1,0)
layout.addWidget(Name,2,0)

layout.addWidget(Salary_Label,3,0)
layout.addWidget(Salary,4,0)

layout.addWidget(Tax_label,5,0)
layout.addWidget(Tax_Amount,6,0)
layout.addWidget(Tax_Amount_box,7,0)
layout.addWidget(Tax_Percent ,8,0)
layout.addWidget(Tax_Percent_box,9,0)

layout.addWidget(sub_text, 10,0)

layout.addWidget(button_1, 21, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignRight)

layout.setContentsMargins(20, 20, 20, 20)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
