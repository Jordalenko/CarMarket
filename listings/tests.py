from django.test import TestCase
from django.urls import reverse

from .models import CarMake, CarModel, Listing


class ListingsFlowTests(TestCase):
	def setUp(self):
		self.make_honda = CarMake.objects.create(name="Honda")
		self.make_toyota = CarMake.objects.create(name="Toyota")
		self.model_civic = CarModel.objects.create(
			name="Civic",
			car_make=self.make_honda,
		)
		self.model_corolla = CarModel.objects.create(
			name="Corolla",
			car_make=self.make_toyota,
		)

		self.honda_listing = Listing.objects.create(
			car_make=self.make_honda,
			car_model=self.model_civic,
			year=2020,
			mileage=20000,
			price=25000,
			fuel_type="Petrol",
		)
		Listing.objects.create(
			car_make=self.make_toyota,
			car_model=self.model_corolla,
			year=2018,
			mileage=40000,
			price=18000,
			fuel_type="Diesel",
		)

	def test_listings_page_filters_results(self):
		response = self.client.get(
			reverse("listings_page"),
			{
				"car_make": "Honda",
				"year": "2020",
				"mileage": "25000",
				"price": "30000",
			},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Honda Civic")
		self.assertNotContains(response, "Toyota Corolla")

		listings = response.context["listings"]
		self.assertEqual(listings.paginator.count, 1)
		self.assertEqual(listings.object_list[0].id, self.honda_listing.id)

	def test_create_listing_form_post_creates_make_model_and_listing(self):
		response = self.client.post(
			reverse("create_listing_form"),
			{
				"car_make": "Mazda",
				"car_model": "MX-5",
				"fuel_type": "Petrol",
				"year": "2022",
				"mileage": "10000",
				"price": "32000",
				"owner_username": "integration-user",
			},
		)

		self.assertEqual(response.status_code, 201)
		self.assertTrue(response.context["result"]["ok"])
		self.assertTrue(response.context["is_success"])

		self.assertTrue(CarMake.objects.filter(name="Mazda").exists())
		self.assertTrue(
			CarModel.objects.filter(
				name="MX-5",
				car_make__name="Mazda",
			).exists()
		)
		self.assertTrue(
			Listing.objects.filter(
				car_make__name="Mazda",
				car_model__name="MX-5",
				year=2022,
				mileage=10000,
				price=32000,
				fuel_type="Petrol",
			).exists()
		)

	def test_create_listing_api_post_returns_json_and_creates_records(self):
		response = self.client.post(
			reverse("create_listing_with_make_model"),
			data={
				"car_make": "BMW",
				"car_model": "M3",
				"year": 2021,
				"mileage": 15000,
				"price": 55000,
				"fuel_type": "Petrol",
				"owner_username": "api-user",
			},
			content_type="application/json",
		)

		self.assertEqual(response.status_code, 201)
		payload = response.json()
		self.assertTrue(payload["ok"])
		self.assertEqual(payload["car_make"]["name"], "BMW")
		self.assertEqual(payload["car_model"]["name"], "M3")
		self.assertEqual(payload["owner"]["username"], "api-user")

		self.assertTrue(CarMake.objects.filter(name="BMW").exists())
		self.assertTrue(
			CarModel.objects.filter(
				name="M3",
				car_make__name="BMW",
			).exists()
		)
		self.assertTrue(
			Listing.objects.filter(
				car_make__name="BMW",
				car_model__name="M3",
				year=2021,
				mileage=15000,
				price=55000,
			).exists()
		)
