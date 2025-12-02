CREATE TABLE potato_group (
    group_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL
);

CREATE TABLE potato_kitchen (
    kitchen_id TEXT PRIMARY KEY,
    group_id TEXT NOT NULL,
    display_name TEXT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES potato_group(group_id)
);

CREATE TABLE potato_user (
    user_id TEXT PRIMARY KEY,
    kitchen_id TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    FOREIGN KEY (kitchen_id) REFERENCES potato_kitchen(kitchen_id)
);

CREATE TABLE potato_recipe (
    recipe_id TEXT PRIMARY KEY,
    version INTEGER NOT NULL,
    state TEXT NOT NULL CHECK(state IN ('DRAFT', 'PUBLISHED', 'ARCHIVED')),
    latest BOOLEAN NOT NULL DEFAULT 1,
    cuisine TEXT,
    description TEXT,
    yield REAL,
    ingredients TEXT NOT NULL, -- JSON blob
    instructions TEXT NOT NULL, -- JSON blob
    created_by TEXT NOT NULL,
    created_timestamp TIMESTAMP NOT NULL,
    last_modified_by TEXT NOT NULL,
    last_modified_timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (created_by) REFERENCES potato_user(user_id),
    FOREIGN KEY (last_modified_by) REFERENCES potato_user(user_id)
);

CREATE TABLE potato_audit (
    audit_id TEXT PRIMARY KEY,
    recipe_id TEXT NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('CREATE', 'ARCHIVE', 'UNARCHIVE', 'EDIT')),
    action_by TEXT NOT NULL,
    action_timestamp TIMESTAMP NOT NULL,
    description TEXT,
    FOREIGN KEY (recipe_id) REFERENCES potato_recipe(recipe_id),
    FOREIGN KEY (action_by) REFERENCES potato_user(user_id)
);
