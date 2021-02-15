## Setup 

`$ virtualenv venv -p python3`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ cd bnpProject`

`$ export FLASK_APP = app.py`

##Unittest
`$ python -m unittest -v`


##Exercises:

## SQL query
```SQL
SELECT PEOPLE.NAME, COMPANIES.NAME
FROM PEOPLE
INNER JOIN COMPANIES ON PEOPLE.COMPANY_ID=CAMPANIES.ID;
```

# task-1
```BASH
$ python -m flask task-1a
```
response: 

`2021-02-15 01:36:28,079  [INFO]  Executing task-1 A ...`
```JSON
[{'author': 'amit',
  'date': '15th february 2017',
  'link': '../review-of-angularjs-grids/',
  'medium': 'https://medium.com/ag-grid/from-hater-to-fan-how-i-fell-in-love-with-ag-grid-3cbc5976d5e3',
  'title': 'From Hater to Fan – How I fell in Love with ag-Grid'},
 {'author': 'john',
  'date': '17th January 2018',
  'link': '../ag-grid-proud-to-support-plunker/',
  'medium': 'https://medium.com/ag-grid/plunker-is-now-backed-by-ag-grid-601c17440fca',
  'title': 'Plunker is now backed by ag-Grid'},
 {'author': 'niall',
  'date': '31st March 2015',
  'link': '../why-the-world-needed-another-angularjs-grid/',
  'medium': 'https://medium.com/ag-grid/why-the-world-needed-another-angularjs-1-x-grid-17e522a53bc8',
  'title': 'Why The World Needed Another AngularJS 1.x Grid'},
 {'author': 'niall',
  'date': '15th September 2015',
  'link': 'https://www.youtube.com/watch?v=jQ_nyTiKbZg',
  'title': 'Angular Air Episode 32: ag-Grid'},
 {'author': 'niall',
  'date': '25th September 2015',
  'link': '../embracing-the-future-with-angularjs2-web-components-and-ag-grid/',
  'medium': 'https://medium.com/ag-grid/embracing-the-future-with-angular-2-0-web-components-and-ag-grid-fec000d5a304',
  'title': 'Embracing the Future with Angular 2.0, Web Components and ag-Grid'},
 {'author': 'niall',
  'date': '21st October 2015',
  'link': 'https://www.youtube.com/watch?v=gNhPeLCBbE0',
  'medium': 'https://medium.com/ag-grid/building-performant-components-for-angularjs-1-x-b4b22c1a3da9',
  'title': 'Building Performant components for AngularJS 1.x'},
 {'author': 'niall',
  'date': '25th October 2015',
  'link': '../ag-grid-in-2016/',
  'medium': 'https://medium.com/ag-grid/stepping-it-up-ag-grid-focuses-on-agnostic-in-2016-fd7cdb8c11d4',
  'title': 'Stepping it Up, ag-Grid Focuses on Agnostic in 2016'},
 {'author': 'niall',
  'date': '28th January 2016',
  'link': '../react-and-ag-grid/',
  'medium': 'https://medium.com/ag-grid/building-a-react-datagrid-using-ag-grid-a-perfect-match-5a4c45f3bedb',
  'title': 'Announcing React and ag-Grid'},
 {'author': 'niall',
  'date': '9th February 2016',
  'link': '../understanding-packaging-for-javascript-typescript-commonjs-and-everything-else/',
  'medium': 'https://medium.com/ag-grid/understand-packaging-for-javascript-typescript-commonjs-and-everything-else-1fe835f3243a',
  'title': 'Understand Packaging for Javascript, TypesScript, CommonJS and '
           'Everything Else'},
 {'author': 'niall',
  'date': '9th March 2016',
  'link': '../ag-grid-goes-commercial/',
  'medium': 'https://medium.com/ag-grid/ag-grid-goes-commercial-3961cf0c6f7b',
  'title': 'ag-Grid Goes Commercial'},
 {'author': 'niall',
  'date': '13th July 2016',
  'link': '../ag-grid-javascript-pivot-grid/',
  'medium': 'https://medium.com/ag-grid/announcing-ag-grid-v5-and-pivot-417fa7649ccb',
  'title': 'Announcing ag-Grid v5 and Pivot'},
 {'author': 'niall',
  'date': '21st September 2016',
  'link': '../ag-grid-angular2-support-v6/',
  'medium': 'https://medium.com/ag-grid/announcing-ag-grid-v6-and-angular-2-datagrid-support-34ceef54872b',
  'title': 'Announcing ag-Grid v6 and Angular 2 Support'},
 {'author': 'niall',
  'date': '5th October 2016',
  'link': '../ag-grid-angular-connect-2016/',
  'medium': 'https://medium.com/ag-grid/were-gonna-need-a-bigger-boat-from-speaker-to-sponsor-with-ag-grid-cf5e01a2d9ba',
  'title': "We're gonna need a bigger boat: from speaker to sponsor with "
           'ag-Grid'},
 {'author': 'niall',
  'date': '27th October 2016',
  'link': '../javascript-datagrid/',
  'medium': 'https://medium.com/ag-grid/8-reasons-to-choose-ag-grid-as-your-javascript-datagrid-eb4a767a351f',
  'title': '8 reasons to choose ag-Grid as your JavaScript Datagrid'},
 {'author': 'niall',
  'date': '19th May 2017',
  'link': '../ag-grid-big-data-small-browser/',
  'medium': 'https://medium.com/ag-grid/delivering-big-data-in-the-small-browser-41704f1058f0',
  'title': 'Big Data / Small Browser'},
 {'author': 'niall',
  'date': '2nd November 2017',
  'link': '../ag-grid-blog-14-0-0/',
  'medium': 'https://medium.com/ag-grid/ag-grid-v14-halloween-released-fb53e674bfc',
  'title': 'ag-Grid v14 Released'},
 {'author': 'sean',
  'date': '30th November 2016',
  'link': '../ag-grid-angular2-support-v7/',
  'medium': 'https://medium.com/ag-grid/ag-grid-v7-aot-angular-2-components-7130fdb8f480',
  'title': 'ag-Grid v7: AOT & Angular 2 Components'},
 {'author': 'sean',
  'date': '8th December 2016',
  'link': '../ag-grid-angular-aot-dynamic-components/',
  'medium': 'https://medium.com/ag-grid/understanding-aot-and-dynamic-components-in-angular-2-9b7548ce5845',
  'title': 'Understanding AOT and Dynamic Components in Angular 2'},
 {'author': 'sean',
  'date': '23rd January 2017',
  'link': '../ag-grid-understanding-webpack/',
  'medium': 'https://medium.com/ag-grid/webpack-tutorial-understanding-how-it-works-f73dfa164f01',
  'title': 'Webpack Tutorial: Understanding How it Works'},
 {'author': 'sean',
  'date': '6th February 2017',
  'link': '../git-color/',
  'medium': 'https://medium.com/ag-grid/git-on-the-command-line-improving-the-experience-5a604cb14cf6',
  'title': 'Git on the Command Line - Improving the Experience'},
 {'author': 'sean',
  'date': '1st March 2017',
  'link': '../vue-js-grid/',
  'medium': 'https://medium.com/ag-grid/using-ag-grid-inside-a-vuejs-application-b6c442d77da8',
  'title': 'VueJS Grid'},
 {'author': 'sean',
  'date': '14th March 2017',
  'link': '../ag-grid-webpack-ngtools/',
  'medium': 'https://medium.com/ag-grid/webpack-tutorial-understanding-ngtools-webpack-306dd7f9e07d',
  'title': 'Webpack Tutorial: Using @ngTools/webpack'},
 {'author': 'sean',
  'date': '13th May 2017',
  'link': '../ag-grid-react-datagrid/',
  'medium': 'https://medium.com/ag-grid/building-a-react-datagrid-with-redux-and-ag-grid-1a837ef1b649',
  'title': 'Building a React Datagrid with Redux and ag-Grid'},
 {'author': 'sean',
  'date': '24th October 2017',
  'link': '../ag-grid-datagrid-crud-part-1/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-1-bf7f9715166e',
  'title': 'Building a CRUD Application with ag-Grid - Part 1'},
 {'author': 'sean',
  'date': '7th November 2017',
  'link': '../ag-grid-datagrid-crud-part-2/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-2-c5e5e4548bf',
  'title': 'Building a CRUD Application with ag-Grid - Part 2'},
 {'author': 'sean',
  'date': '21st November 2017',
  'link': '../ag-grid-datagrid-crud-part-3/',
  'title': 'Building a CRUD Application with ag-Grid - Part 3'},
 {'author': 'sean',
  'date': '5th December 2017',
  'link': '../ag-grid-datagrid-crud-part-4/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-4-3189034df922',
  'title': 'Building a CRUD Application with ag-Grid - Part 4'},
 {'author': 'sophia',
  'date': '14th November 2017',
  'link': '../ag-grid-blog-14-2-0/',
  'medium': 'https://medium.com/ag-grid/whats-new-in-ag-grid-v14-2-0-6cf06f953109',
  'title': "What's New in ag-Grid v14.2.0"},
 {'author': 'sophia',
  'date': '13th December 2017',
  'link': '../ag-grid-blog-15-0-0/',
  'medium': 'https://medium.com/ag-grid/happy-new-ag-grid-v15-0-0-698f3f405069',
  'title': 'Happy New ag-Grid v15.0.0'},
 {'author': 'sophia',
  'date': '22nd January 2018',
  'link': '../ag-grid-blog-16-0-0/',
  'medium': 'https://medium.com/ag-grid/introducing-version-16-phoenix-and-our-new-website-53403451083c',
  'title': 'Introducing Version 16: Phoenix and Our New Website'},
 {'author': 'sophia',
  'date': '27th February 2018',
  'link': '../best-react-grid-blog/',
  'title': 'Meet the Best React Grid'
}]
```

```BASH
$ python -m flask task-1b 
```
response:

`2021-02-15 01:37:43,358  [INFO]  Executing task-1 B ...`
```JSON
[{'author': 'sophia',
  'date': '2018-01-22',
  'link': '../ag-grid-blog-16-0-0/',
  'medium': 'https://medium.com/ag-grid/introducing-version-16-phoenix-and-our-new-website-53403451083c',
  'title': 'Introducing Version 16: Phoenix and Our New Website'},
 {'author': 'sophia',
  'date': '2018-02-27',
  'link': '../best-react-grid-blog/',
  'title': 'Meet the Best React Grid'},
 {'author': 'john',
  'date': '2018-01-17',
  'link': '../ag-grid-proud-to-support-plunker/',
  'medium': 'https://medium.com/ag-grid/plunker-is-now-backed-by-ag-grid-601c17440fca',
  'title': 'Plunker is now backed by ag-Grid'},
 {'author': 'sophia',
  'date': '2017-12-13',
  'link': '../ag-grid-blog-15-0-0/',
  'medium': 'https://medium.com/ag-grid/happy-new-ag-grid-v15-0-0-698f3f405069',
  'title': 'Happy New ag-Grid v15.0.0'},
 {'author': 'sean',
  'date': '2017-12-05',
  'link': '../ag-grid-datagrid-crud-part-4/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-4-3189034df922',
  'title': 'Building a CRUD Application with ag-Grid - Part 4'},
 {'author': 'sean',
  'date': '2017-11-21',
  'link': '../ag-grid-datagrid-crud-part-3/',
  'title': 'Building a CRUD Application with ag-Grid - Part 3'},
 {'author': 'sophia',
  'date': '2017-11-14',
  'link': '../ag-grid-blog-14-2-0/',
  'medium': 'https://medium.com/ag-grid/whats-new-in-ag-grid-v14-2-0-6cf06f953109',
  'title': "What's New in ag-Grid v14.2.0"},
 {'author': 'sean',
  'date': '2017-11-07',
  'link': '../ag-grid-datagrid-crud-part-2/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-2-c5e5e4548bf',
  'title': 'Building a CRUD Application with ag-Grid - Part 2'},
 {'author': 'niall',
  'date': '2017-11-02',
  'link': '../ag-grid-blog-14-0-0/',
  'medium': 'https://medium.com/ag-grid/ag-grid-v14-halloween-released-fb53e674bfc',
  'title': 'ag-Grid v14 Released'},
 {'author': 'sean',
  'date': '2017-10-24',
  'link': '../ag-grid-datagrid-crud-part-1/',
  'medium': 'https://medium.com/ag-grid/building-a-crud-application-with-ag-grid-part-1-bf7f9715166e',
  'title': 'Building a CRUD Application with ag-Grid - Part 1'},
 {'author': 'niall',
  'date': '2017-05-19',
  'link': '../ag-grid-big-data-small-browser/',
  'medium': 'https://medium.com/ag-grid/delivering-big-data-in-the-small-browser-41704f1058f0',
  'title': 'Big Data / Small Browser'},
 {'author': 'sean',
  'date': '2017-05-13',
  'link': '../ag-grid-react-datagrid/',
  'medium': 'https://medium.com/ag-grid/building-a-react-datagrid-with-redux-and-ag-grid-1a837ef1b649',
  'title': 'Building a React Datagrid with Redux and ag-Grid'},
 {'author': 'sean',
  'date': '2017-03-14',
  'link': '../ag-grid-webpack-ngtools/',
  'medium': 'https://medium.com/ag-grid/webpack-tutorial-understanding-ngtools-webpack-306dd7f9e07d',
  'title': 'Webpack Tutorial: Using @ngTools/webpack'},
 {'author': 'sean',
  'date': '2017-03-01',
  'link': '../vue-js-grid/',
  'medium': 'https://medium.com/ag-grid/using-ag-grid-inside-a-vuejs-application-b6c442d77da8',
  'title': 'VueJS Grid'},
 {'author': 'amit',
  'date': '2017-02-15',
  'link': '../review-of-angularjs-grids/',
  'medium': 'https://medium.com/ag-grid/from-hater-to-fan-how-i-fell-in-love-with-ag-grid-3cbc5976d5e3',
  'title': 'From Hater to Fan – How I fell in Love with ag-Grid'},
 {'author': 'sean',
  'date': '2017-02-06',
  'link': '../git-color/',
  'medium': 'https://medium.com/ag-grid/git-on-the-command-line-improving-the-experience-5a604cb14cf6',
  'title': 'Git on the Command Line - Improving the Experience'},
 {'author': 'sean',
  'date': '2017-01-23',
  'link': '../ag-grid-understanding-webpack/',
  'medium': 'https://medium.com/ag-grid/webpack-tutorial-understanding-how-it-works-f73dfa164f01',
  'title': 'Webpack Tutorial: Understanding How it Works'},
 {'author': 'sean',
  'date': '2016-12-08',
  'link': '../ag-grid-angular-aot-dynamic-components/',
  'medium': 'https://medium.com/ag-grid/understanding-aot-and-dynamic-components-in-angular-2-9b7548ce5845',
  'title': 'Understanding AOT and Dynamic Components in Angular 2'},
 {'author': 'sean',
  'date': '2016-11-30',
  'link': '../ag-grid-angular2-support-v7/',
  'medium': 'https://medium.com/ag-grid/ag-grid-v7-aot-angular-2-components-7130fdb8f480',
  'title': 'ag-Grid v7: AOT & Angular 2 Components'},
 {'author': 'niall',
  'date': '2016-10-27',
  'link': '../javascript-datagrid/',
  'medium': 'https://medium.com/ag-grid/8-reasons-to-choose-ag-grid-as-your-javascript-datagrid-eb4a767a351f',
  'title': '8 reasons to choose ag-Grid as your JavaScript Datagrid'},
 {'author': 'niall',
  'date': '2016-10-05',
  'link': '../ag-grid-angular-connect-2016/',
  'medium': 'https://medium.com/ag-grid/were-gonna-need-a-bigger-boat-from-speaker-to-sponsor-with-ag-grid-cf5e01a2d9ba',
  'title': "We're gonna need a bigger boat: from speaker to sponsor with "
           'ag-Grid'},
 {'author': 'niall',
  'date': '2016-09-21',
  'link': '../ag-grid-angular2-support-v6/',
  'medium': 'https://medium.com/ag-grid/announcing-ag-grid-v6-and-angular-2-datagrid-support-34ceef54872b',
  'title': 'Announcing ag-Grid v6 and Angular 2 Support'},
 {'author': 'niall',
  'date': '2016-07-13',
  'link': '../ag-grid-javascript-pivot-grid/',
  'medium': 'https://medium.com/ag-grid/announcing-ag-grid-v5-and-pivot-417fa7649ccb',
  'title': 'Announcing ag-Grid v5 and Pivot'},
 {'author': 'niall',
  'date': '2016-03-09',
  'link': '../ag-grid-goes-commercial/',
  'medium': 'https://medium.com/ag-grid/ag-grid-goes-commercial-3961cf0c6f7b',
  'title': 'ag-Grid Goes Commercial'},
 {'author': 'niall',
  'date': '2016-02-09',
  'link': '../understanding-packaging-for-javascript-typescript-commonjs-and-everything-else/',
  'medium': 'https://medium.com/ag-grid/understand-packaging-for-javascript-typescript-commonjs-and-everything-else-1fe835f3243a',
  'title': 'Understand Packaging for Javascript, TypesScript, CommonJS and '
           'Everything Else'},
 {'author': 'niall',
  'date': '2016-01-28',
  'link': '../react-and-ag-grid/',
  'medium': 'https://medium.com/ag-grid/building-a-react-datagrid-using-ag-grid-a-perfect-match-5a4c45f3bedb',
  'title': 'Announcing React and ag-Grid'},
 {'author': 'niall',
  'date': '2015-10-25',
  'link': '../ag-grid-in-2016/',
  'medium': 'https://medium.com/ag-grid/stepping-it-up-ag-grid-focuses-on-agnostic-in-2016-fd7cdb8c11d4',
  'title': 'Stepping it Up, ag-Grid Focuses on Agnostic in 2016'},
 {'author': 'niall',
  'date': '2015-10-21',
  'link': 'https://www.youtube.com/watch?v=gNhPeLCBbE0',
  'medium': 'https://medium.com/ag-grid/building-performant-components-for-angularjs-1-x-b4b22c1a3da9',
  'title': 'Building Performant components for AngularJS 1.x'},
 {'author': 'niall',
  'date': '2015-09-25',
  'link': '../embracing-the-future-with-angularjs2-web-components-and-ag-grid/',
  'medium': 'https://medium.com/ag-grid/embracing-the-future-with-angular-2-0-web-components-and-ag-grid-fec000d5a304',
  'title': 'Embracing the Future with Angular 2.0, Web Components and ag-Grid'},
 {'author': 'niall',
  'date': '2015-09-15',
  'link': 'https://www.youtube.com/watch?v=jQ_nyTiKbZg',
  'title': 'Angular Air Episode 32: ag-Grid'},
 {'author': 'niall',
  'date': '2015-03-31',
  'link': '../why-the-world-needed-another-angularjs-grid/',
  'medium': 'https://medium.com/ag-grid/why-the-world-needed-another-angularjs-1-x-grid-17e522a53bc8',
  'title': 'Why The World Needed Another AngularJS 1.x Grid'}]

```

# task-2

```BASH
$ python -m flask run
```

http://127.0.0.1:5000/average

response:
```JSON
{
    average: 112.73986526015811,
    period: "all_data"
}
```

http://127.0.0.1:5000/average?from=2015-03-25&to=2015-06-30

response:
```JSON
{
    average: 127.6266200132353,
    period: {
        from: "2015-03-25",
        to: "2015-06-30"
    }
}
```
