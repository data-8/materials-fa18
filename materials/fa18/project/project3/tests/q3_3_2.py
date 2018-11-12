test = {
  'name': 'Question 3.1.3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')
          True
          >>> test_movie_correctness.num_rows == test_movies.num_rows
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> print(test_movie_correctness.group('Genre'))
          Genre   | count
          action  | 21
          romance | 16
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
