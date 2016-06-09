from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required
from ..models import User
from forms import AddProductForm, AddCategoryForm
from . import admin
from .. import db
from ..models import Category, Product

@admin.route('/add-product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Product(name = form.name.data,
                    description=form.description.data,
                    price=form.price.data,
                    category_id=form.category.data, stock=form.stock.data)
        db.session.add(new_product)
        db.session.commit()
        flash('You have successfully added a new product.')
        return redirect(url_for('admin.add_product'))
    return render_template('admin/add_product.html', form=form, title="Add Product")

@admin.route('/add-category', methods=['GET', 'POST'])
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        cat_exist = Category.query.filter_by(name=form.name.data).first()
        if not cat_exist:
            new_category = Category(name=form.name.data,description=form.description.data)
            db.session.add(new_category)
            db.session.commit()
            flash('You have successfully added a new category.')
         #   flash('This Category Exists, add a new category.')
        return redirect(url_for('admin.add_category'))

    return render_template('admin/add_category.html', form=form, title="Add Category")



@admin.route('/view', methods=['GET', 'POST'])
def view():
        products = Product.query.all()
        return render_template('admin/view.html', products=products, table=products, title="Products")

@admin.route('/edit-product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    products = Product.query.get(id)
    # if current_user.id != issue.user_id:
    #   abort(403)
    form = AddProductForm(obj=products)
    if form.validate_on_submit():
        products.name = form.name.data
        products.description = form.description.data
        products.category_id = form.category.data
        products.price = form.price.data
        products.stock = form.stock.data
        db.session.add(products)

        db.session.commit()

        return redirect(url_for('admin.view'))
    form.name.data = products.name
    form.description.data = products.description
    form.price.data = products.price
    form.category.data= products.category_id
    form.stock= products.stock
    #flash('You have successfully updated product.')
    return render_template('admin/edit_product.html', form=form, title="Edit Product")


@admin.route('/delete-product/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    products = Product.query.get(id)
    # if current_user.id != issue.user_id:
    #   abort(403)
    form = AddProductForm(obj=products)
    db.session.delete(products)
    db.session.commit()
    return redirect(url_for('admin.view'))
    return render_template('admin/delete_product.html', products=products, title="Delete Product")
