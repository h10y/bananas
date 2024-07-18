from shiny import App, render, reactive, ui
import functions

# Libraries for data and SVM model
import pandas as pd
from joblib import load
from sklearn import svm

# Plot Libraries
from shinywidgets import output_widget, register_widget

# Global
x = pd.read_csv('bananas.csv')
classes = ['Under', 'Ripe', 'Very', 'Over']

svm_model = load('bananas-svm.joblib') 

app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            12,
            ui.h1("Banana AI"),
        )
    ),
    ui.row(
        ui.column(
            2,
            ui.h2("Settings"),
            ui.p("Enter color values."),
            ui.input_numeric(
                "green",
                label = "Green",
                value = 0.2,
                min = 0,
                max = 1,
                step = 0.01
            ),
            ui.input_numeric(
                "yellow",
                label = "Yellow",
                value = 0.7,
                min = 0,
                max = 1,
                step = 0.01
            ),
            ui.input_numeric(
                "brown",
                label = "Brown",
                value = 0.1,
                min = 0,
                max = 1,
                step = 0.01
            )
        ),
        ui.column(
            6,
            output_widget(
                "ternary", 
                width="100%", # doesn't seem to do anything
            ),
        ),
        ui.column(
            4,
            ui.h2("Prediction"),
            ui.output_ui("ripeness_txt"),
            output_widget(
                "bars", 
                width = "100%", # doesn't seem to do anything
            )
        )
    ),
    title = "Banana AI",
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    ternary = functions.go.FigureWidget(
        data=[
            functions.trace_fun(x[x.ripeness == "Under"], "#576a26", "Under"),
            functions.trace_fun(x[x.ripeness == "Ripe"], "#eece5a", "Ripe"),
            functions.trace_fun(x[x.ripeness == "Very"], "#966521", "Very"),
            functions.trace_fun(x[x.ripeness == "Over"], "#261d19", "Over"),
            functions.trace_fun(pd.DataFrame([{
                'green': 0,
                'yellow': 0,
                'brown': 0,
                'ripeness': "Ripe"
            }]), "red", "New point", highlight = True)
        ],
        layout={
            'margin': {
                'b': 40,
                'l': 60,
                't': 40,
                'r': 10
            },
            'ternary': {
                'sum': 1,
                'aaxis': functions.axis_fun('Green'),
                'baxis': functions.axis_fun('Yellow'),
                'caxis': functions.axis_fun('Brown'),
                'bgcolor': "white",
            },
            'height': 400,
        },
    )

    bars = functions.go.FigureWidget(
        data=[
            functions.go.Bar({
                'x': classes,
                'y': [0,0,0,0],
                'marker': {'color': ["#576a26", "#eece5a", "#966521", "#261d19"]},
            })
        ],
        layout={
            "showlegend": False, 
            'xaxis_title': 'Ripeness', 
            'yaxis_title': 'Probability',
            'margin': {
                'b': 0,
                'l': 60,
                't': 35,
                'r': 10
            },
            'height': 200
        },
    )
    bars.update_layout(plot_bgcolor="white")
    bars.update_xaxes(linecolor='rgba(100,100,100,1)')
    bars.update_yaxes(gridcolor='rgba(230,230,230,1)')

    register_widget("ternary", ternary)
    register_widget("bars", bars)

    @reactive.Calc
    def pred():
        print(f"G={input.green()} / Y={input.yellow()} / B={input.brown()}")

        prediction = svm_model.predict_proba([[
                                        functions.cast_to_float(input.green()), 
                                        functions.cast_to_float(input.yellow()),
                                        functions.cast_to_float(input.brown())
                                    ]])
        print(prediction[0])

        return prediction[0], classes[list(prediction[0]).index(max(prediction[0]))]

    @reactive.Effect
    def _():
        ternary.data[4].a = [functions.cast_to_float(input.green())]
        ternary.data[4].b = [functions.cast_to_float(input.yellow())]
        ternary.data[4].c = [functions.cast_to_float(input.brown())]

        bars.data[0].y = pred()[0] 

    @output
    @render.ui
    def ripeness_txt():
        ripeness = {
            "Under": "under ripe",
            "Ripe": "ripe",
            "Very": "very ripe",
            "Over": "over ripe"
        }
        return ui.TagList(
            ui.p(
                "The banana is ",
                ui.strong(ripeness[pred()[1]])
            )
        )

app = App(app_ui, server)
