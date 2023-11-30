```mermaid
erDiagram
  Movie {
    Integer id PK
    String title
    String release_date
    Float popularity
    Integer vote_count
    Float vote_average
    Text overview
    String poster_path
    Boolean adult
    Null genres FK
  }

  Genre {
    Integer id PK
    String name
    Null movies FK
  }

  Movie ||--|{ Genre : has
```