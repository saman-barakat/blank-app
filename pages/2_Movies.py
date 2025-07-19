import matplotlib.pyplot as plt

# Sample dataset: Movie titles and their box office earnings (in millions)
movies = ['Inception', 'Titanic', 'Avengers', 'Joker', 'Frozen']
earnings = [829, 2187, 2798, 1074, 1276]

plt.figure(figsize=(8, 5))
plt.bar(movies, earnings, color='skyblue')
plt.title('Box Office Earnings of Movies')
plt.xlabel('Movie')
plt.ylabel('Earnings (in millions USD)')
plt.tight_layout()
plt.show()