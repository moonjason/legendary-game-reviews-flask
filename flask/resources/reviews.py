import models
import requests
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
review = Blueprint('reviews', 'review')

@review.route("/", methods=["GET"])
def get_all_reviews():
  try:
    reviews = [model_to_dict(reviews) for reviews in models.Review.select()]
    print(reviews)
    return jsonify(data=reviews, status={"code": 201, "message": "Success"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@review.route("/", methods=["POST"])
def add_review():
  payload = request.get_json()
  print(payload, "<----this is the payload ")
  review = models.Review.create(**payload)
  print(review.__dict__)
  return jsonify(data=model_to_dict(review), status={"code": 201, "message": "success"})

@review.route("/<id>/edit", methods=["PUT"])
def edit_review(id):
  payload = request.get_json()
  print(payload)
  query = models.Review.update(**payload).where(models.Review.id == id)
  query.execute()
  review = models.Review.get_by_id(id)
  return jsonify(data=model_to_dict(review), status={"code": 201, "message": "Success"})

@review.route('/<id>', methods=["DELETE"])
def delete_review(id):
    query = models.Review.delete().where(models.Review.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})