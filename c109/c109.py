import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import csv
import pandas as pd 
df = pd.read_csv("StudentsPerformance.csv")
dice_result = df["reading score"].tolist()
mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
first_std_deviation_start,first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start,second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)
fig = ff.create_distplot([dice_result],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_end],y=[0,0.17],mode = "lines",name = "STDEV1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_end],y=[0,0.17],mode = "lines",name = "STDEV2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_end],y=[0,0.17],mode = "lines",name = "STDEV3"))
fig.show()
print(mean)
print(mode)
print(median)
print(std_deviation)