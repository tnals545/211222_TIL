import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Movie from "../components/Movie";

function Detail() {
  const { id } = useParams();
  const [movies, setMovies] = useState([]);
  const getMovie = async () => {
    const json = await (
      await fetch(
        `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year&movie_id=${id}`
      )
    ).json();
    setMovies(json.data.movies);
  };
  useEffect(() => {
    getMovie();
  }, []);
  return (
    <div>
      {movies.map((movie) => {
        if (movie.id === parseInt(id)) {
          return (
            <Movie
              key={movie.id}
              id={movie.id}
              coverImg={movie.medium_cover_image}
              title={movie.title}
              summary={movie.summary}
              genres={movie.genres}
            />
          );
        } else {
          return null;
        }
      })}
    </div>
  );
}
export default Detail;
