<script>
    import { JsonView } from '@zerodevx/svelte-json-view'
    import { onMount } from 'svelte';

    import recipeClient from '$lib/service/recipe-client';

    let error = $state(true);
    let errorMessage = $state("");
    let data = $state([]);

    onMount(() => {

        recipeClient.listRecipes()
            .then((status) => {
                data = status;
                error = false;
            })
            .catch((err) => {
                error = true;
                errorMessage = err.message;
            });
    });

</script>

{#if error}
    <p class="error">Error: {errorMessage}</p>
{:else}
    <table class="cyber-table cyber-style-2">
        <thead>
            <tr>
                <th>Name</th>
                <th>Version</th>
                <th>State</th>
                <th>Cuisine</th>
                <th>Yield</th>
                <th># Ingredients</th>
                <th># Instructions</th>
            </tr>
        </thead>
        <tbody>
            {#each data as recipe}
                <tr>
                    <td><a href={`/recipe/${recipe.recipe_id}`}>{recipe.description}</a></td>
                    <td>{recipe.version}</td>
                    <td>{recipe.state}</td>
                    <td>{recipe.cuisine}</td>
                    <td>{recipe.yield}</td>
                    <td>{JSON.parse(recipe.ingredients).length}</td>
                    <td>{JSON.parse(recipe.instructions).length}</td>
                </tr>
            {/each}
        </tbody>

    </table>

    <JsonView json={data} />
{/if}
