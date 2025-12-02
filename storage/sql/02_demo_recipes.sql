-- Note: AI Generated for ~speed~

-- 10 demo recipes with UUIDs and structured JSON ingredients & instructions

INSERT INTO potato_recipe (
    recipe_id, version, state, latest,
    cuisine, description, yield,
    ingredients, instructions,
    created_by, created_timestamp,
    last_modified_by, last_modified_timestamp
)
VALUES
(
 '9c8de286-1037-4c1c-a9fd-0bb068f8a70d', 1, 'PUBLISHED', 1,
 'Italian', 'Classic spaghetti with tomato sauce.', 4,
 '[
    { "ingredient_id": 1, "ingredient_name": "Spaghetti", "type": "grain", "quantity": 200, "quantity_units": "g" },
    { "ingredient_id": 2, "ingredient_name": "Tomato Sauce", "type": "sauce", "quantity": 1, "quantity_units": "cup" },
    { "ingredient_id": 3, "ingredient_name": "Salt", "type": "seasoning", "quantity": 1, "quantity_units": "tsp" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Boil the spaghetti until al dente.", "timing_s": 600 },
    { "instruction_id": 2, "ingredients": [2], "instruction_body": "Warm the tomato sauce in a saucepan.", "timing_s": 300 },
    { "instruction_id": 3, "ingredients": [1,2,3], "instruction_body": "Combine spaghetti and sauce. Season with salt.", "timing_s": -1 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 '3e3bb966-7b65-4f0f-8c67-c5127b4e8f71', 1, 'PUBLISHED', 1,
 'Mexican', 'Easy chicken tacos.', 3,
 '[
    { "ingredient_id": 1, "ingredient_name": "Tortillas", "type": "grain", "quantity": 6, "quantity_units": "pcs" },
    { "ingredient_id": 2, "ingredient_name": "Cooked Chicken", "type": "meat", "quantity": 1, "quantity_units": "cup" },
    { "ingredient_id": 3, "ingredient_name": "Lettuce", "type": "vegetable", "quantity": 0.5, "quantity_units": "cup" },
    { "ingredient_id": 4, "ingredient_name": "Salsa", "type": "sauce", "quantity": 0.25, "quantity_units": "cup" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Warm the tortillas.", "timing_s": 60 },
    { "instruction_id": 2, "ingredients": [2], "instruction_body": "Shred the cooked chicken.", "timing_s": -1 },
    { "instruction_id": 3, "ingredients": [1,2,3,4], "instruction_body": "Assemble tacos with chicken, lettuce, and salsa.", "timing_s": -1 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 '06560db4-3b85-4435-b9c2-fb9a1cba2091', 1, 'PUBLISHED', 1,
 'American', 'Cheeseburger with toppings.', 2,
 '[
    { "ingredient_id": 1, "ingredient_name": "Ground Beef", "type": "meat", "quantity": 1, "quantity_units": "lb" },
    { "ingredient_id": 2, "ingredient_name": "Cheese Slice", "type": "dairy", "quantity": 2, "quantity_units": "pcs" },
    { "ingredient_id": 3, "ingredient_name": "Buns", "type": "grain", "quantity": 2, "quantity_units": "pcs" },
    { "ingredient_id": 4, "ingredient_name": "Lettuce", "type": "vegetable", "quantity": 2, "quantity_units": "leaves" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Form beef into patties and season.", "timing_s": -1 },
    { "instruction_id": 2, "ingredients": [1], "instruction_body": "Grill patties until cooked through.", "timing_s": 480 },
    { "instruction_id": 3, "ingredients": [2,3,4], "instruction_body": "Assemble burger with cheese and toppings.", "timing_s": -1 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 'c33c0976-7d47-4b31-a4e8-a2a7c0fea2df', 1, 'PUBLISHED', 1,
 'Indian', 'Simple chickpea curry.', 4,
 '[
    { "ingredient_id": 1, "ingredient_name": "Chickpeas", "type": "legume", "quantity": 1, "quantity_units": "can" },
    { "ingredient_id": 2, "ingredient_name": "Curry Paste", "type": "seasoning", "quantity": 2, "quantity_units": "tbsp" },
    { "ingredient_id": 3, "ingredient_name": "Coconut Milk", "type": "dairy", "quantity": 1, "quantity_units": "cup" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1,2], "instruction_body": "Heat curry paste and chickpeas in a pan.", "timing_s": 300 },
    { "instruction_id": 2, "ingredients": [3], "instruction_body": "Add coconut milk and simmer.", "timing_s": 600 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 'b1cb1ed8-d7e5-4e55-a22c-9a1f0046073d', 1, 'PUBLISHED', 1,
 'Japanese', 'Teriyaki chicken bowl.', 2,
 '[
    { "ingredient_id": 1, "ingredient_name": "Chicken Thighs", "type": "meat", "quantity": 0.75, "quantity_units": "lb" },
    { "ingredient_id": 2, "ingredient_name": "Teriyaki Sauce", "type": "sauce", "quantity": 0.5, "quantity_units": "cup" },
    { "ingredient_id": 3, "ingredient_name": "Rice", "type": "grain", "quantity": 1, "quantity_units": "cup" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Cook chicken thighs in a skillet.", "timing_s": 600 },
    { "instruction_id": 2, "ingredients": [1,2], "instruction_body": "Add teriyaki sauce and simmer.", "timing_s": 300 },
    { "instruction_id": 3, "ingredients": [3], "instruction_body": "Cook and plate rice.", "timing_s": -1 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 '0156d8ca-69eb-49d3-9622-e52f2ddcdb2b', 1, 'PUBLISHED', 1,
 'French', 'Basic omelette.', 1,
 '[
    { "ingredient_id": 1, "ingredient_name": "Eggs", "type": "dairy", "quantity": 2, "quantity_units": "pcs" },
    { "ingredient_id": 2, "ingredient_name": "Butter", "type": "dairy", "quantity": 1, "quantity_units": "tbsp" },
    { "ingredient_id": 3, "ingredient_name": "Salt", "type": "seasoning", "quantity": 0.25, "quantity_units": "tsp" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Beat the eggs in a bowl.", "timing_s": -1 },
    { "instruction_id": 2, "ingredients": [2], "instruction_body": "Melt butter in a pan.", "timing_s": 60 },
    { "instruction_id": 3, "ingredients": [1,3], "instruction_body": "Pour in eggs and cook until set.", "timing_s": 180 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 '62557e05-23c3-462f-b6aa-b864c556d055', 1, 'PUBLISHED', 1,
 'Thai', 'Basic Pad Thai.', 2,
 '[
    { "ingredient_id": 1, "ingredient_name": "Rice Noodles", "type": "grain", "quantity": 200, "quantity_units": "g" },
    { "ingredient_id": 2, "ingredient_name": "Egg", "type": "dairy", "quantity": 1, "quantity_units": "pcs" },
    { "ingredient_id": 3, "ingredient_name": "Bean Sprouts", "type": "vegetable", "quantity": 1, "quantity_units": "cup" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1], "instruction_body": "Soak rice noodles in warm water.", "timing_s": 900 },
    { "instruction_id": 2, "ingredients": [2], "instruction_body": "Scramble the egg.", "timing_s": 180 },
    { "instruction_id": 3, "ingredients": [1,2,3], "instruction_body": "Combine all ingredients in wok and stir fry.", "timing_s": 300 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 'cf31f712-c8ac-4a83-b958-af047bccf043', 1, 'PUBLISHED', 1,
 'Greek', 'Fresh Greek salad.', 3,
 '[
    { "ingredient_id": 1, "ingredient_name": "Tomato", "type": "vegetable", "quantity": 1, "quantity_units": "pcs" },
    { "ingredient_id": 2, "ingredient_name": "Cucumber", "type": "vegetable", "quantity": 1, "quantity_units": "pcs" },
    { "ingredient_id": 3, "ingredient_name": "Feta", "type": "dairy", "quantity": 0.5, "quantity_units": "cup" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1,2], "instruction_body": "Chop tomato and cucumber.", "timing_s": -1 },
    { "instruction_id": 2, "ingredients": [3], "instruction_body": "Top with feta.", "timing_s": -1 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 'd7050851-84c0-4c4b-b581-90b2f06f88fa', 1, 'PUBLISHED', 1,
 'Mediterranean', 'Smooth hummus dip.', 6,
 '[
    { "ingredient_id": 1, "ingredient_name": "Chickpeas", "type": "legume", "quantity": 1, "quantity_units": "can" },
    { "ingredient_id": 2, "ingredient_name": "Tahini", "type": "paste", "quantity": 2, "quantity_units": "tbsp" },
    { "ingredient_id": 3, "ingredient_name": "Garlic", "type": "vegetable", "quantity": 1, "quantity_units": "clove" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [1,2,3], "instruction_body": "Blend all ingredients until smooth.", "timing_s": 120 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
),
(
 'ef2bc21e-3c1a-4b70-8cfa-cc42de44d12a', 1, 'PUBLISHED', 1,
 'Chinese', 'Vegetable stir fry.', 4,
 '[
    { "ingredient_id": 1, "ingredient_name": "Mixed Vegetables", "type": "vegetable", "quantity": 2, "quantity_units": "cup" },
    { "ingredient_id": 2, "ingredient_name": "Soy Sauce", "type": "sauce", "quantity": 2, "quantity_units": "tbsp" },
    { "ingredient_id": 3, "ingredient_name": "Oil", "type": "fat", "quantity": 1, "quantity_units": "tbsp" }
 ]',
 '[
    { "instruction_id": 1, "ingredients": [3], "instruction_body": "Heat oil in a pan.", "timing_s": 60 },
    { "instruction_id": 2, "ingredients": [1], "instruction_body": "Add vegetables and stir fry.", "timing_s": 300 },
    { "instruction_id": 3, "ingredients": [2], "instruction_body": "Add soy sauce and mix well.", "timing_s": 60 }
 ]',
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'),
 '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now')
);

-- Audit entries for all 10 recipes
INSERT INTO potato_audit (audit_id, recipe_id, action, action_by, action_timestamp, description) VALUES
('be4f904e-738b-4f7a-852d-fd0bb7cb74a0', '9c8de286-1037-4c1c-a9fd-0bb068f8a70d', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('2b57fa6c-4a0c-46d9-bf54-268ad40bb56d', '3e3bb966-7b65-4f0f-8c67-c5127b4e8f71', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('ff9bc4ea-3298-4aef-9500-eb2a796a33b7', '06560db4-3b85-4435-b9c2-fb9a1cba2091', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('d2f8dfb2-bf4d-4e34-a708-321e83a2667c', 'c33c0976-7d47-4b31-a4e8-a2a7c0fea2df', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('873478ee-1e5e-4072-9750-3b8d623fd2ce', 'b1cb1ed8-d7e5-4e55-a22c-9a1f0046073d', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('c2b229dc-4c4d-4d70-a920-32df6b95dc40', '0156d8ca-69eb-49d3-9622-e52f2ddcdb2b', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('5cc10d28-7bb9-4b38-8b5c-2bb22486ff47', '62557e05-23c3-462f-b6aa-b864c556d055', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('b6f0ef04-1ad4-4386-a7e0-e92e4c428b88', 'cf31f712-c8ac-4a83-b958-af047bccf043', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('f6a03346-8a63-4dd9-bdac-4a90acf188c4', 'd7050851-84c0-4c4b-b581-90b2f06f88fa', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation'),
('7dcc3c20-485e-4a70-b606-e5e9bc4f2411', 'ef2bc21e-3c1a-4b70-8cfa-cc42de44d12a', 'CREATE', '6af1737a-b33a-4ae1-8962-0c0893c5ac65', datetime('now'), 'Initial creation');
