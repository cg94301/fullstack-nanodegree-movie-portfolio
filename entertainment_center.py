import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

martian = media.Movie("The Martian",
                      "A story of survival on Mars",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

ted = media.Movie("Ted",
                  "Story about a real live teddy bear",
                  "https://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",
                  "https://www.youtube.com/watch?v=3Vl5q06UElM")

argo = media.Movie("Argo",
                   "Story about Iran hostage situation",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSJ2MeWRy5_BxYPmP2ZvZ1n8CmkKaG95TUC7lRkfaRpfqbZlY9U",
                   "https://www.youtube.com/watch?v=w918Eh3fij0")

monkeys = media.Movie("12 Monkeys",
                      "A story about time travel and saving the world",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcSVWaLbGRL7p1T1OR767o6HU_J6wZd2nqzZFG7Pp7VtxCF8fgQH",
                      "https://www.youtube.com/watch?v=15s4Y9ffW_o")


movies = [toy_story, avatar, martian, ted, argo, monkeys]

fresh_tomatoes.open_movies_page(movies)
