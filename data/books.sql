CREATE TABLE
    IF NOT EXISTS books (
        id VARCHAR(36) PRIMARY KEY,
        title VARCHAR(255) UNIQUE,
        summary TEXT,
        ISBN BIGINT UNSIGNED,
        genre VARCHAR(255),
        publication_year INT UNSIGNED,
        author VARCHAR(255),
        publisher VARCHAR(255) NULL,
        rating FLOAT
    )
    
INSERT INTO
    books (
        id,
        title,
        summary,
        ISBN,
        genre,
        publication_year,
        author,
        publisher,
        rating
    )
VALUES
    (
        "e8c7c561-bc25-46f2-8b27-5ea8d42a9c5e",
        "Harry Potter and the Sorcerer's Stone",
        "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he's a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.After a lifetime of bottling up his magical powers, Harry finally feels like a normal kid. But even within the Wizarding community, he is special. He is the boy who lived: the only person to have ever survived a killing curse inflicted by the evil Lord Voldemort, who launched a brutal takeover of the Wizarding world, only to vanish after failing to kill Harry.Though Harry's first year at Hogwarts is the best of his life, not everything is perfect. There is a dangerous secret object hidden within the castle walls, and Harry believes it's his responsibility to prevent it from falling into evil hands. But doing so will bring him into contact with forces more terrifying than he ever could have imagined.Full of sympathetic characters, wildly imaginative situations, and countless exciting details, the first installment in the series assembles an unforgettable magical world and sets the stage for many high-stakes adventures to come.",
        9780439554930,
        "Fantasy, Magic",
        1997,
        "J.K. Rowling",
        "Scholastic",
        4.4
    ),
    (
        "26e3e8a8-a882-4a97-b06a-48c4b2f7eac6",
        "To Kill a Mockingbird",
        "Set in the Deep South during the 1930s, this Pulitzer Prize-winning novel follows a young girl's experience of racial injustice in a small Alabama town. As she witnesses her father, a lawyer, defend a wrongly accused black man, she learns valuable lessons about prejudice, empathy, and understanding.",
        9780061120084,
        "Fiction, Classics",
        1960,
        "Harper Lee",
        "J.B. Lippincott & Co.",
        4.7
    ),
    (
        "b6a7c3b6-2398-49c1-a6c0-4ee7a5e7bfc0",
        "The Invisible Man",
        "Written in 1949, this dystopian novel depicts a totalitarian future society where the government exercises total control over its citizens. The story follows Winston Smith, a low-ranking member of the ruling Party, as he begins to question the official ideology and eventually rebels against the system, risking his life and sanity.",
        9780486284728,
        "Science Fiction, Classics",
        1897,
        "H.G. Wells",
        "Pearson's Magazine",
        4.1
    ),
    (
        "7bab5cff-6b86-4027-891e-b41441261b9e",
        "The Nightingale",
        "Set in France during World War II, this historical fiction novel tells the story of two sisters, Vianne and Isabelle, as they navigate the difficulties and dangers of living under German occupation. While Vianne tries to maintain a sense of normalcy and protect her young daughter, Isabelle joins the French Resistance, risking everything to fight against the Nazis.",
        9781250066197,
        "Historical Fiction, War",
        2015,
        "Kristin Hannah",
        "St. Martin's Press",
        4.8
    ),
    (
        "f2541876-7025-4bb1-ac7c-e30f664ed919",
        "The Hitchhiker's Guide to the Galaxy",
        "When Earth is destroyed to make way for a hyperspace bypass, unwitting human Arthur Dent hitches a ride on a passing spaceship. He embarks on a misadventure-filled journey through space and time, accompanied by his friend Ford Prefect, an alien researching Earth for the titular guidebook.",
        9781400052929,
        "Science Fiction, Comedy",
        1979,
        "Douglas Adams",
        "Pan Books",
        4.4
    )