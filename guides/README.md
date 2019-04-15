### [Guides](https://mateja.lasan.ca/guides)

#### Purpose.

I set out to create an app where I could showcase a collection of written guides for issues,
problems, or techniques that I have learned over the past few years. The main idea was for me to
have the ability to write a guide in markdown format, label it under a specific tag, and have the
website format it into a simple looking, legible guide. Just like it says on the main page of the
app, "after becoming more comfortable with the situation, I like to write a guide on how I would go
about solving it." This app is where I plan to host these guides.

#### Resources.

When deciding on a design for the guides app, I felt it would be best to keep it simple. My
original idea was to keep it simple enough to show in a printed newspaper, with the only thing
different being a darker colour scheme, with white font. In general, the guides app is under-
styled. I do have some plans for changing it in the future, but at the moment I think leaving it
under-styled is far better than having a distracting layout.

#### Problems and lessons.

The guides app featured two main problems, the first being similar to that in the résumé app;
recursively rendering a family tree for tags and their sub-tags. You can read about the solution to the first issue [here](https://github.com/matootie/mateja.lasan.ca/tree/master/resume#problems-and-lessons). The other issue stemmed directly
from the first.

Initially, the URL scheme for the guides app would use follow as such:

`https://mateja.lasan.ca/guides/<tag value>/<guide name>`

`https://mateja.lasan.ca/guides/python/using-mongodb-with-django`

Because two different tags of the same value could be classified under different parent tags, there
was no way for the URL handler to differentiate between "Server Management / Python," and "Web
Development / Python," for example. The unappealing but straightforward solution was to use tag IDs
in the URL scheme, as this was certain to be unique.

`https://mateja.lasan.ca/guides/<tag id>/<guide id>`

`https://mateja.lasan.ca/guides/1/4`
