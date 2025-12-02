<script>
    import { JsonView } from '@zerodevx/svelte-json-view'
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    import recipeClient from '$lib/service/recipe-client';

    let error = $state(true);
    let errorMessage = $state("");
    let data = $state({"hello": "world"});

    onMount(() => {
        recipeClient.getRecipe($page.params.recipe_id || "unknown")
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

<h3 class="cyber-h">Raw Recipe JSON</h3>

{#if error}
    <p class="error">Error: {errorMessage}</p>
{:else}
    <JsonView json={data} />
{/if}
