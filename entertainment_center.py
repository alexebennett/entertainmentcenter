# Import media file that contains the class Movie
import media

# Import fresh_tomatoes.py file that contains html, css, and  open_movies_page function
import fresh_tomatoes

# Instances of favourite movies to be displayed
a_new_hope = media.Movie("Star Wars: A New Hope",
                         "The Imperial Forces -- under orders from cruel Darth Vader (David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker (Mark Hamill) and Han Solo (Harrison Ford), captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 (Kenny Baker) and C-3PO (Anthony Daniels) to rescue the beautiful princess, help the Rebel Alliance, and restore freedom and justice to the Galaxy.",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                         "https://www.youtube.com/watch?v=nywPf1p-BBY",
                         "27 October 1977",
                         "Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing, Alec Guinness")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                         "The adventure continues in this Star Wars sequel. Luke Skywalker (Mark Hamill), Han Solo (Harrison Ford), Princess Leia (Carrie Fisher) and Chewbacca (Peter Mayhew) face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth. While Han and Leia escape in the Millennium Falcon, Luke travels to Dagobah in search of Yoda. Only with the Jedi master's help will Luke survive when the dark side of the Force beckons him into the ultimate duel with Darth Vader (David Prowse).",
                         "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                         "https://www.youtube.com/watch?v=xESiohGGP7g",
                         "7 August 1980",
                         "Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, Frank Oz")

return_of_the_jedi = media.Movie("Return of the Jedi",
                         "Luke Skywalker (Mark Hamill) battles horrible Jabba the Hut and cruel Darth Vader to save his comrades in the Rebel Alliance and triumph over the Galactic Empire. Han Solo (Harrison Ford) and Princess Leia (Carrie Fisher) reaffirm their love and team with Chewbacca, Lando Calrissian (Billy Dee Williams), the Ewoks and the androids C-3PO and R2-D2 to aid in the disruption of the Dark Side and the defeat of the evil emperor.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                         "https://www.youtube.com/watch?v=MYD_xxY5wEI",
                         "27 October 1983",
                         "Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, Frank Oz")

house_of_cards = media.Movie("House of Cards",
                         "House of Cards is an American political drama web television series created by Beau Willimon. ... Set in 2010s Washington, D.C., House of Cards is the story of Congressman Frank Underwood (Kevin Spacey), a Democrat from South Carolina's 5th congressional district and House Majority Whip.",
                         "https://s-media-cache-ak0.pinimg.com/736x/6c/84/a5/6c84a5c9a41368677a67bba992ec643e.jpg",
                         "https://www.youtube.com/watch?v=UW8Zyt8SF_U",                      
                         "February 1, 2013",
                         "Kevin Spacey, Robin Wright, Kate Mara, Corey Stoll, Michael Kelly, Sakina Jaffrey, Kristen Connolly, Sebastian Arcelus, Michel Gill, Nathan Darrow, Rachel Brosnahan, Constance Zimmer, Mahershala Ali")

narcos = media.Movie("Narcos",
                         "The first season of Narcos, an American crime thriller drama web television series produced and created by Chris Brancato, Carlo Bernard, and Doug Miro, follows the story of notorious drug kingpin Pablo Escobar, who became a billionaire through the production and distribution of cocaine, while also focusing on Escobar's interactions with drug lords, DEA agents, and various opposition entities.",
                         "http://www.impawards.com/tv/posters/narcos_xlg.jpg",
                         "https://www.youtube.com/watch?v=TKFxCPBUPa8",
                         "August 28, 2015",
                         "Wagner Moura, Boyd Holbrook, Pedro Pascal, Joanna Christie, Luis Guzmán, André Mattos, Roberto Urbina, Diego Cataño, Jorge A. Jimenez, Paulina Gaitán, Paulina García, Stephanie Sigman, Damian Alcazar, Martina García, Luis Gnecco")

the_sopranos = media.Movie("The Sopranos",
                         "The Sopranos is an American crime drama television series created by David Chase. The story revolves around the fictional character, New Jersey-based Italian American mobster Tony Soprano (James Gandolfini). The Sopranos is widely regarded as one of the greatest television series of all time.",
                         "http://onesheetdesign.com/wp-content/uploads/The_Sopranos.jpg",
                         "https://www.youtube.com/watch?v=wrN2k3qGbVA",
                         "January 10, 1999",
                         "James Gandolfini, Lorraine Bracco, Edie Falco, Michael Imperioli, Dominic Chianese, Steven Van Zandt, Tony Sirico, Robert Iler, Jamie-Lynn Sigler")

big_lebowski = media.Movie("The Big Lebowski",
                         "Jeff Bridges plays Jeff Lebowski who insists on being called the Dude, a laid-back, easygoing burnout who happens to have the same name as a millionaire whose wife owes a lot of dangerous people a whole bunch of money -- resulting in the Dude having his rug soiled, sending him spiraling into the Los Angeles underworld.",
                         "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                         "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                         "March 6, 1998",
                         "Jeff Bridges, John Goodman, Julianne Moore, Steve Buscemi, David Huddleston, John Turturro")

american_history_x = media.Movie("American History X",
                         "Living a life marked by violence and racism, neo-Nazi Derek Vinyard (Edward Norton) finally goes to prison after killing two black youths who tried to steal his car. Upon his release, Derek vows to change his ways; he hopes to prevent his younger brother, Danny (Edward Furlong), who idolizes Derek, from following in his footsteps. As he struggles with his own deeply ingrained prejudices and watches their mother grow sicker, Derek wonders if his family can overcome a lifetime of hate.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                         "https://www.youtube.com/watch?v=XfQYHqsiN5g",
                         "October 30, 1998",
                         "Edward Norton, Edward Furlong, Fairuza Balk, Stacy Keach, Elliott Gould, Avery Brooks, Beverly D'Angelo")

ali = media.Movie("Ali",
                         "With wit and athletic genius, with defiant rage and inner grace, Muhammad Ali forever changed the American landscape. Fighting all comers, Ali took on the law, conventions, the status quo and the war -- as well as the fists in front of him. Ali both ignited and mirrored the conflicts of his time and ours to become one of the most admired fighters in the world. Forget, now, what you thought you knew.",
                         "https://upload.wikimedia.org/wikipedia/en/3/3d/Ali_movie_poster.jpg",
                         "https://www.youtube.com/watch?v=STuHQ5HpmEE",
                         "December 25, 2001",
                         "Will Smith, Jamie Foxx, Jon Voight, Mario Van Peebles, Ron Silver, Jeffrey Wright, Mykelti Williamson, James Toney")

resovoir_dogs = media.Movie("Resovoir Dogs",
                         "A group of thieves assemble to pull of the perfect diamond heist. It turns into a bloody ambush when one of the men turns out to be a police informer. As the group begins to question each other's guilt, the heightening tensions threaten to explode the situation before the police step in.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
                         "https://www.youtube.com/watch?v=vayksn4Y93A",                      
                         "January 21, 1992",
                         "Harvey Keitel, Tim Roth, Chris Penn, Steve Buscemi, Lawrence Tierney, Michael Madsen")

citizenfour = media.Movie("Citizenfour",
                         "After Laura Poitras received encrypted emails from someone with information on the government's massive covert-surveillance programs, she and reporter Glenn Greenwald flew to Hong Kong to meet the sender, who turned out to be Edward Snowden.",
                         "https://upload.wikimedia.org/wikipedia/en/3/37/Citizenfour_poster.jpg",
                         "https://www.youtube.com/watch?v=XiGwAvd5mvM",
                         "October 10, 2014",
                         "Edward Snowden, Glenn Greenwald, William Binney, Jacob Appelbaum, Ewen MacAskill")

manufacturing_consent = media.Movie("Manufacturing Consent",
                         "Manufacturing Consent: Noam Chomsky and the Media is a 1992 documentary film that explores the political life and ideas of linguist, intellectual, and political activist Noam Chomsky. Canadian filmmakers Mark Achbar and Peter Wintonick expand the analysis of political economy and mass media presented in Manufacturing Consent, a 1988 book Chomsky coauthored with Edward S. Herman.",
                         "https://upload.wikimedia.org/wikipedia/en/1/11/Manufacturing_Consent_movie_poster.jpg",
                         "https://www.youtube.com/watch?v=7LVsiP0s33A",
                         "1992",
                         "Mark Achbar, Noam Chomsky")

# Favourite movies arrange in an array
movies = [a_new_hope, empire_strikes_back, return_of_the_jedi, house_of_cards, narcos, the_sopranos, big_lebowski, american_history_x, ali, resovoir_dogs, citizenfour, manufacturing_consent]

# Directing array to fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
