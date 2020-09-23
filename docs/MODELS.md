Belts
    - Degree                (1st gup, 2nd Degree, etc.)
    - Color
    - Eligibility
    - Terminology           (foreign key to Terminology)
    - Dodging               (foreign key to Dodges)
    - Stances               (foreign key to Stances)
    - Blocks                (foreign key to Blocks)
    - Hyung                 (Foreign key to Hyung)
    - Hand Techniques       (Foreign key to Hand Techniques)
    - Leg Techniques        (Foreign key to Leg Techniques)
    - Combinations          (Foreign key to Combinations)
    - JuJutstu              (Foreign key to JuJutsu)
    - Sparring
    - Breaking

Terminology
    - Term
    - Description

Dodges
    - Name
    - Description
    - Video URL???

Stances
    - Name
    - Description
    - Image URL???

Blocks
    - Name
    - Description
    - Video URL???

Hyung
    - Name
    - Description
    - Video URL!!!

    - Hand Techniques   (ManyToMany foreign key to Hand Techniques) (Future feature???)
    - Leg Techniques    (ManyToMany Field to Leg Techniques) (Future feature???)
    - Stances           (ManyToMany Field to Stances) (Maybe???)

Hand Techniques
    - Name
    - Description
    - Video URL???

Leg Techniques
    - Name
    - Description
    - Video URL???

Combinations
    - Name
    - Description

    - Hand Techniques   (ManyToMany foreign key to Hand Techniques) (Future feature???)
    - Leg Techniques    (ManyToMany foreign key to Leg Techniques) (Future feature???)
    - Video URL???

JuJutsu
    - Name
    - Description

Breaking
    - Name
    - Description

    - Hand Techniques   (ManyToMany foreign key to Hand Techniques) (Future feature???)
    - Leg Techniques    (ManyToMany foreign key to Leg Techniques) (Future feature???)
    - Video URL???