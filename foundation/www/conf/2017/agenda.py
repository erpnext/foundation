# -*- coding: utf-8 -*-

from __future__ import unicode_literals

def get_context(context):
	context.agenda = [
		dict(
			title = 'Day 1: Developer Talks',
			items = [
				dict(time='10am-11am',
					title='Frappé Framework Architecture and Way Forward',
					description='Overview of the architecture of Frappé and the direction in which we are going'),
				dict(time='11am-12pm',
					title='Developing the User Interface',
					description='Understanding controls, views, layouts, and other objects in the Frappé User Interface'),
				dict(time='12pm-1pm',
					title='Debugging Frappé',
					description='Tips and tricks on how to debug client and serverside issues in Frappé'),
				dict(time='1pm-2pm',
					title='Lunch'),
				dict(time='2pm-3pm',
					title='Designing Portals in Frappé',
					description='How to build web views, web forms, customize templates and other website related topics'),
				dict(time='3pm-4pm',
					title='Deployment and Release',
					description='Understanding the Frappé release process and best practices for deployment and updating'),
				dict(time='4pm-5pm',
					title='Contributing to ERPNext',
					description='Contributing best practices, writing tests, updating docs and planning your contributions')

			]
		),
		dict(
			title = 'Day 2: ERPNext Roadmap',
			items = [
				dict(time='10am-11am',
					title='ERPNext Roadmap',
					description='Taking a look at the most requested features in ERPNext and how do we prioritize them'),
				dict(time='11am-12pm',
					title='Localizations',
					description='How to design and contribute extensions for legal requirements for different countries.'),
				dict(time='12pm-1pm',
					title='Integrations',
					description='How to build and contribute 3rd party integrations in ERPNext.'),
				dict(time='1pm-2pm',
					title='Lunch'),
				dict(time='2pm-5pm',
					title='Module Analysis',
					description='In this session will will look at each ERPNext module including Accounting, Manufacturing, CRM etc and discuss what should be the priority development in each of these modules')
			]
		),
		dict(
			title = 'Day 3: Community and User Talks',
			items = [
				dict(time='10am-11am',
					title='Welcome and ERPNext Foundation',
					description='A look back at what we have achieved in the 6 months and what is the vision for the ERPNext Foundation'),
				dict(time='11am-12pm',
					title='Business of ERPNext',
					description='A panel discussion on how to make money on ERPNext and build a sustainable eco-system'),
				dict(time='12pm-1pm',
					title='User Stories',
					description='Three ERPNext Users will share their ERPNext Journeys'),
				dict(time='1pm-2pm',
					title='Lunch'),
				dict(time='2pm-3pm',
					title='Feature Showcase',
					description='Three developers from the community will showcase the extensions they have built on ERPNext'),
				dict(time='3pm-4pm',
					title='The Road Ahead',
					description='Panel Disussion with Gold Members on how do we make ERPNext a mainstream ERP alternative to paid ERPs'),
				dict(time='4pm-5pm',
					title='Lightening Talks and Q&A',
					description='5 min lightening talks by the audience and Q&A with the foundation members'),

			]
		)
	]