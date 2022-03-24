import plotly.express as px
import pandas


def collatz(n):
    steps = 0
    sequenz = [(0, n)]
    current_number = n
    while current_number != 1:
        steps += 1
        if current_number % 2 == 0:
            current_number = current_number // 2
            sequenz.append((steps, current_number))
        else:
            current_number = current_number * 3 + 1
            sequenz.append((steps, current_number))
    return sequenz


def main():
    sequenz = collatz(27)
    sequenz_raw = [x[1] for x in sequenz]
    steps_raw = [x[0] for x in sequenz]
    df = px.data.gapminder()
    fig = px.line(df, x=steps_raw, y=sequenz_raw)
    fig.show()


if __name__ == '__main__':
    main()
