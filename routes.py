from app import app, db1
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime, date
import models
import forms

@app.route('/')
@app.route('/index')
def index():
    print('in Index')
    events1 = models.Event1.query.all()
    return render_template('home_page.html', events1=events1)

@app.route('/landing')
def landing():
    print('in Landing')
    return render_template('landing.html')

@app.route('/login')
def login():
    print('in Login')
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    print('in Sign Up')
    return render_template('sign_up.html')

@app.route('/contact')
def contact():
    print('in Contact')
    return render_template('contact.html')

@app.route('/about')
def about():
    print('in About')
    return render_template('about.html')

@app.route('/services')
def services():
    print('in Services')
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    print('in Testimonials')
    return render_template('testimonials.html')

@app.route('/your_events')
def your_events():
    events1 = models.Event1.query.all()
    return render_template('your_events.html', events1=events1)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddEventForm()
    if form.validate_on_submit():
        event = models.Event(title=form.title.data, date=datetime.utcnow())
        db1.session.add(event)
        db1.session.commit()
        flash('Event added')
        print("Added Event", form.title.data, event.title, event.date)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/add1')
def dummyphone():
    print("In dummyphone")
    return render_template('create_event1.html')

@app.route('/add1', methods=['GET', 'POST'])
def add1():
    print("In add1")
    event_name  = request.form['event_name']
    event_date = request.form['event_date']
    print("The Event Date is", event_date)
    event1 = models.Event1(event_name=event_name, event_date=event_date)
    db1.session.add(event1)
    print('Event added')
    db1.session.commit()
    print('Event committed')
    return redirect('/')

@app.route('/edit1/<int:event_id>')
def dummyedit(event_id):
    print("In dummyedit")
    event = models.Event1.query.get(event_id)
    return render_template('edit_event.html', value=event)

@app.route('/edit1/<int:event_id>', methods=['GET', 'POST'])
def edit1(event_id):
    print("In edit1")
    event = models.Event1.query.get(event_id)
    print(event)
    event_name = request.form['event_name']
    print("The Event Name is", event_name)
    event_date = request.form['event_date']
    print("The Event Date is", event_date)
    if event:
        event.event_name = event_name
        event.event_date = event_date
        db1.session.commit()
        print('Event updated')
        return redirect(url_for('home_page.html'))
    print(f'Event with id {event_id} does not exit')
    return redirect(url_for('home_page.html'))

@app.route('/delete1/<int:event_id>', methods=['GET', 'POST'])
def delete1(event_id):
    print("In delete1")
    event1 = models.Event1.query.get(event_id)
    if event1:
        db1.session.delete(event1)
        db1.session.commit()
        print('Event1 deleted')
    flash(f'Event with id {event_id} does not exit')
    return redirect(url_for('index'))

@app.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit(event_id):
    form = forms.AddEventForm()
    event = models.Event.query.get(event_id)
    print(event)
    form.date.data = datetime.utcnow()
    if event:
        if form.validate_on_submit():
            event.title = form.title.data
            event.date = datetime.utcnow()
            db1.session.commit()
            flash('Event updated')
            return redirect(url_for('index'))
        print ("Edit Form Event", form.title.data)
        form.title.data = event.title
        return render_template('edit.html', form=form, event_id=event_id)
    flash(f'Event with id {event_id} does not exit')
    return redirect(url_for('index'))


@app.route('/delete/<int:event_id>', methods=['GET', 'POST'])
def delete(event_id):
    form = forms.DeleteEventForm()
    event = models.Event.query.get(event_id)
    if event:
        if form.validate_on_submit():
            if form.submit.data:
                db1.session.delete(event)
                db1.session.commit()
                flash('Event deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, event_id=event_id, title=event.title)
    flash(f'Event with id {event_id} does not exit')
    return redirect(url_for('index'))


