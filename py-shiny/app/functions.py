import plotly.graph_objects as go

# functions
def axis_fun(title):
    return {
        'title': title,
        'titlefont': {
            'size': 20
        },
        'tickfont': {
            'size': 15
        },
        'tickcolor': 'rgba(0,0,0,0)',
        'ticklen': 5,
        'linecolor': 'rgba(100,100,100,1)',
        'gridcolor': 'rgba(200,200,200,1)',
    }

def trace_fun(data, color, name, highlight = False):
    return go.Scatterternary({
            'mode': 'markers',
            # 'data': data,
            'a': data['green'],
            'b': data['yellow'],
            'c': data['brown'],
            'text': data['ripeness'],
            'name': name,
            'marker': {
                'opacity': 0.75,
                'color': color,
                'size': 14,
                'line': {
                    'width': 2,
                    'color': "red" if highlight else color
                }
            }
        })
        
def cast_to_float(i):
    return float(0 if i is None else i)
