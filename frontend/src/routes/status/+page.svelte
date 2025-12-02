<script>
    import { JsonView } from '@zerodevx/svelte-json-view'
    import { onMount } from 'svelte';

    import recipeClient from '$lib/service/recipe-client';

    let error = $state(true);
    let errorMessage = $state("");
    let data = $state({"hello": "world"});

    onMount(() => {
        recipeClient.getStatus()
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

<h3 class="cyber-h">Backend Connection Status</h3>

{#if error}
    <p class="error">Error: {errorMessage}</p>
{:else}
    <p>Connection successful. Backend status data:</p>
    <JsonView json={data} />
{/if}
