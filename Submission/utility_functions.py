import pandas as pd
import matplotlib.pyplot as plt
import itertools

def plot_activity_counts(df):
    
    # Count occurrences of each activity code
    activity_counts = df['activity'].value_counts().sort_index()
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(activity_counts.index, activity_counts.values, color='blue')
    plt.xlabel('Activity Code')
    plt.ylabel('Number of Rows')
    plt.title('Activity Code Frequency')
    plt.xticks(activity_counts.index)  # Ensure all activity codes are displayed
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Display the values on top of the bars
    for index, value in enumerate(activity_counts.values):
        plt.text(activity_counts.index[index], value + 0.1, str(value), ha='center', fontsize=12)
    plt.show()


def plot_subject_counts(df):
   
    # Count occurrences of each activity code
    subject_counts = df['subject'].value_counts().sort_index()
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(subject_counts.index, subject_counts.values, color='blue')
    plt.xlabel('Subject Code')
    plt.ylabel('Number of Rows')
    plt.title('Subject Code Frequency')
    plt.xticks(subject_counts.index)  # Ensure all activity codes are displayed
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Display the values on top of the bars
    for index, value in enumerate(subject_counts.values):
        plt.text(subject_counts.index[index], value + 0.1, str(value), ha='center', fontsize=12)
    plt.show()


def group_features_by_prefix(features):
    feature_groups = {}
    
    for feature in features:
        prefix = "_".join(feature.split("_")[:2])  # Extract first two parts
        if prefix not in feature_groups:
            feature_groups[prefix] = []
        feature_groups[prefix].append(feature)
    
    return feature_groups
