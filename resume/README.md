### [Resume](https://mateja.lasan.ca/resume)

* [Purpose.](#purpose)
* [Resources.](#resources)
* [Problems and lessons.](#problems-and-lessons)

#### Purpose.

The app was intended to be a more involving format for my résumé
featuring images, colours, and animations; All of which you would not
usually want to include. Additionally, most of the work I do currently is
with web development and design; however, all of the other things that I
do, be it music, film, or game development, can be found online as well.
Having an online résumé format would make it incredibly easy to showcase
the work that I have done, in a more elegant way than printing hyperlinks
on to a piece of paper.

#### Resources.

There are only two significant design features in the résumé app; The
first being how some element animations are triggered on viewport entry,
and the second being the smooth parallax scrolling effect on some parts
of the background.

The animation effects were created using simple CSS3 animations, and the
functionality of determining when they enter the viewport was produced
using jQuery.

The parallax scrolling effect was taken from an open-sourced repository
you can find [here](https://github.com/pixelcog/parallax.js/).

If you would like to see the source code for the résumé app, you can find
it [here](https://github.com/matootie/mateja.lasan.ca/tree/master/resume).

#### Problems and lessons.

One of the features I wanted in my online résumé was to be able to list
computer skills under existing computer skills. For example, I would like
to include that I am skilled at using the Django Web Framework, but I
would prefer to sort it below Python on a list, as a "sub-skill" of
Python. Then, I would like to include that I am skilled at using the
Django REST Framework, which I would prefer to sort under Django. This
kind of nested parenting caused a bit of an issue in the app templates.

The problem with rendering this in the app templates was that there was
no way of knowing how long a specific computer skills family line was. I
ended up having to recursively loop through a template until there were
no more child skills left, which was finally done like this:

```html
<!-- resume/main.html -->

{% for computer_skill in computer_skills %}
    {% with depth=0 computer_skill=computer_skill template_name="resume/base/subskill.html" %}
        {% include template_name %}
    {% endwith %}
{% endfor %}
```

```html
<!-- resume/base/subskill.html -->

<div>
    <p>{{ computer_skill.name }}</p>
</div>

{% if computer_skill.subskills %}
    {% for subskill in computer_skill.subskills.all %}
        {% with new_depth=depth|add:1 %}
            {% with depth=new_depth computer_skill=subskill template_name="resume/base/subskill.html" %}
                {% include template_name %}
            {% endwith %}
        {% endwith %}
    {% endfor %}
{% endif %}
```

You can see that I kept track of a depth value, which was only used in
CSS as an indentation factor. It is also important to note that I have
taken out a large portion of the HTML formatting and classes from this
example, as well as the "proficiency" functionality as it does not
pertain to or affect the family tree issue.
