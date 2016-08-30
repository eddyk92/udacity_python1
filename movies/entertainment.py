import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life", 
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=d1_JBMrrYw8")	
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", 
							 "Using rock music to learn",
							 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "htpps://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", 
						  "A rat is a chef in Paris",
						  "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						  "htpps://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
								"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								"htpps://www.youtube.com/watch?v=atLg2wQQxvU")
hunger_games = media.Movies("Hunger Games",
							"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
							"htpps://www.youtube.com/watch?v=PbA63a7HObo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games ]
fresh_tomatoes.open_movies_page(movies)