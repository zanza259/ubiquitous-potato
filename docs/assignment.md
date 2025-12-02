## Design & Architect a "Recipe Management System"

#### Product Requirements
- Keep track of recipes for a kitchen. A recipe should consist of a list of ingredients, instructions to combine those ingredients, and yield information (how much food does the recipe produce).
- Allow users to search for recipes.
- Display recipes in a way that is easy for someone working in a kitchen to see/understand.
- Allow users to edit or remove recipes.

#### Architectural Requirements
- Needs to handle no more than 5,000 to 10,000 requests per day.
- Will store no more than 1,000 recipes.
- May have several dozen users across different (potentially competing) restaurants.
- Don’t worry about things like internationalization.

#### Deliverables
- Skeleton out the system (backend and frontend)
- You can skeleton out authentication, but this doesn’t need to be implemented
- More concerned with seeing how you structure and test your code
- Consider error conditions and border cases, but stay within the time window!

- Design/architecture document in your choice (markdown is perfectly fine)
    - Considerations or any interesting decisions that went into your design choices (for example, maintainability, cost, language, etc)
    - Sending a github link (or repo/source) and any screenshots


## Requirement Clarifications

> Should I assume that that the product requirements are for a deployed web app and any end users don't have specific connectivity requirements?

Correct! Yeah, just a standard web app. No particular connectivity. I guess ideally it would work on a typical Internet connection (or even phone).
 
>Is there any standardization around units being used both for ingredients and for the output yields? (Volume / weight / etc).

This is a great question and not at all. In fact, assume that some things could be grams, others pounds, others quarts, etc. Also the units might end up being different for input ingredients and output yields!
 
> Are there any relevant timing components for recipe steps that should be included (thinking simmer for 20minutes before next step type of thing).

That's also a good question. I think a set of instructions is a great idea (in addition to perhaps notes).
 
> In terms of "search for recipes" are there any requirements on what can be searched on? (Name / categorization / ingredients content / etc)?

Not at all, whatever you think is best here. Name is probably sufficient, although in the past we have wanted to filter on both category and ingredient.
 
> Mentioning 5k to 10k requests per day, are those bursty (around rush hours for instance) or more of a consistent qps?

Another good question, I would say they would tend to be bursty, but a bit unpredictable. Likely it would be more around when new shifts start or they change what they are prepping.

Not a requirement, but something that might be interesting to think about is how other services would access this data -- if it's worth thinking of some kind of notification system when things change.
 
> Are users allowed to create recipes as well as edit/remove them?

Yes!
 
> Are edits/removals instanced per restaurant or location? (Ie, if restaurant A deletes the "burrito" because of some local reason, does that disappear also for all other sites/users or only for the site/user in question?)

Good question. I would say per-location, as in my experience, recipes are shared across all 'restaurants/brands' in our Pittsburgh facility, but are subtly different in our other facilities. Plus I sort of like thinking about recipes as abstracted from restaurants.
 
> Similarly - are all of the recipes instanced or restricted at all in this way? Italian restaurant can only access Italian recipes for instance?

This gets more complex, but you could perhaps see a location having sub locations, in which the sub locations share some recipes with the parent, but add additional recipes of their own. But this might be too much for this prototype. 
 
> Are there any specific requirements around change control and auditing of the modifications made to recipes?

Auditing is great! Just having a simple audit log is good enough for this, I think.