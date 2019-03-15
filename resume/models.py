"""
All the models needed for the online resume.
"""

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Something happened here

class Skill(models.Model):
    """
    A model representing a resume skill.

    description: A description of what the skill entails.
    """

    description = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the skill object.

        :return: the skill object's description.
        """

        return f"{self.description[:15]}..."

    class Meta:
        """
        Meta properties of the resume skills model.
        """

        verbose_name = "Resume Skill"
        verbose_name_plural = "Resume Skills"


class ComputerSkill(models.Model):
    """
    A model representing a computer related skill.

    name: The name of the skill.
    proficiency: Confidence with the skill, out of 100.
    """

    name = models.CharField(max_length=140)
    proficiency = models.IntegerField()

    def __str__(self):
        """
        String representation of the computer skill object.

        :return: the computer skill object's name.
        """

        return f"{self.name}"

    class Meta:
        """
        Meta properties of the computer skills model.
        """

        ordering = ("-proficiency",)
        verbose_name = "Computer Skill"
        verbose_name_plural = "Computer Skills"


class Location(models.Model):
    """
    A model representing a location,
    for use in the work experience model.

    city: The city.
    province: The province or state.
    country: The country.
    """

    city = models.CharField(max_length=140)
    province = models.CharField(max_length=140)
    country = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the Location object.

        :return: The location object's city, province and country.
        """

        return f"{self.city}, {self.province}, {self.country}"

    class Meta:
        """
        Meta properties of the location model.
        """

        ordering = (
            "country",
            "province",
            "city")
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Experience(models.Model):
    """
    A model representing a type of experience

    location: A location object containing the job location.
    """

    location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        """
        Meta properties of the experience model.
        """

        abstract = True


class EducationExperience(Experience):
    """
    A model representing education history.

    institution: The institution I attended.
    accreditation: The accreditation I received (Diploma, Degree, Certificate).
    """

    institution = models.CharField(max_length=140)
    accreditation = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the education object.

        :return: The education object's accreditation and institution
        """

        return f"{self.accreditation}, {self.institution}"

    class Meta:
        """
        Meta properties for the education model.
        """

        verbose_name = "Educational Credibility"
        verbose_name_plural = "Educational Credibility's"


class WorkExperience(Experience):
    """
    A model representing work experience.

    position: The position of the job.
    employer: Who employed me.
    """

    position = models.CharField(max_length=140)
    employer = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the work experience object.

        :return: The work experience object's position and employer.
        """

        return f"{self.position}, {self.employer}"

    class Meta:
        """
        Meta properties of the work experience model.
        """

        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"


class VolunteerExperience(Experience):
    """
    A model representing volunteer work.

    recipient: The foundation or organization that I volunteered for.
    """

    recipient = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the volunteer work object.

        :return: The volunteer work object's recipient.
        """

        return f"{self.recipient}"

    class Meta:
        """
        Meta properties for the volunteer model.
        """

        verbose_name = "Volunteer Experience"
        verbose_name_plural = "Volunteer Experiences"


class CoverLetter(models.Model):
    """
    A model representing cover letters.

    text: The text content of the cover letter.
    """

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the cover letter object.

        :return: The first 10 characters of the cover letter object's text.
        """
        
        return f"{self.text[:10]}..."


    class Meta:
        """
        Meta properties of the cover letter model.
        """

        ordering = ('-created', )
        verbose_name = "Cover Letter"
        verbose_name_plural = "Cover Letters"


'''
class Task(models.Model):
    """
    A model representing a work task.
    """

    details = models.CharField(max_length=140)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    experience = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        """
        String representation of the task object.

        :return: The first 5 characters of the task object's details.
        """

        return f"{self.details[:15]}..."

    class Meta:
        """
        Meta properties for the task model.
        """

        ordering = ("content_type",)
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
'''
