def count_papers(academics):
    return sum([len(academic['papers']) for academic in academics])

def list_papers(academics):
    paper_list = []
    for academic in academics:
        paper_list += academic['papers']
    return paper_list

academics = [
    {
        'name': 'Alice',
        'papers': [
            {
                'title': 'My science paper',
                'date': 2015
            },
            {
                'title': 'My other science paper',
                'date': 2017
            }
        ]
    },
    {
        'name': 'Bob',
        'papers': [
            {
                'title': 'Bob writes about science',
                'date': 2018
            }
        ]
    }
]

print(list_papers(academics))