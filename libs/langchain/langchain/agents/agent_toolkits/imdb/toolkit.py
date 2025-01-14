from typing import List

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.tools import BaseTool
from langchain.tools.imdb.cast_of_movie import IMDbCastOfMovie
from langchain.tools.imdb.get_movie_crew import IMDbGetMovieCrew
from langchain.tools.imdb.get_movie_info import IMDbGetMovieInfo
from langchain.tools.imdb.get_person_bio import IMDbGetPersonBio
from langchain.tools.imdb.get_person_movies import IMDbGetPersonMovies
from langchain.tools.imdb.plot_of_movie import IMDbPlotOfMovie
from langchain.tools.imdb.popular_movies import IMDbPopularMovies
from langchain.tools.imdb.search_keyword import IMDbSearchMovieKeyword
from langchain.tools.imdb.search_movie import IMDbSearchMovie
from langchain.tools.imdb.search_person import IMDbSearchPerson


class IMDbToolkit(BaseToolkit):
    """Toolkit for interacting with IMDB."""

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            IMDbCastOfMovie(),
            IMDbGetMovieCrew(),
            IMDbGetMovieInfo(),
            IMDbGetPersonBio(),
            IMDbGetPersonMovies(),
            IMDbPopularMovies(),
            IMDbPlotOfMovie(),
            IMDbSearchMovie(),
            IMDbSearchPerson(),
            IMDbSearchMovieKeyword(),
        ]
