-- Note: AI Generated for ~speed~

-- Demo group
INSERT INTO potato_group (group_id, display_name)
VALUES ('8f1df1a7-1e55-4ff7-a4b7-1d705c44b4f1', 'Demo Group');

-- Demo kitchen
INSERT INTO potato_kitchen (kitchen_id, group_id, display_name)
VALUES (
    '2c8e6bd0-5bfc-4f61-b1b5-4aa613edef4b',
    '8f1df1a7-1e55-4ff7-a4b7-1d705c44b4f1',
    'Demo Kitchen'
);

-- Demo user
INSERT INTO potato_user (user_id, kitchen_id, first_name, last_name)
VALUES (
    '6af1737a-b33a-4ae1-8962-0c0893c5ac65',
    '2c8e6bd0-5bfc-4f61-b1b5-4aa613edef4b',
    'Demo',
    'User'
);
