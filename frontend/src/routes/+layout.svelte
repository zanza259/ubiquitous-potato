<script>
	import favicon from '$lib/assets/favicon.svg';
	import Icon from '$lib/components/icon/index.svelte';
	import Avatar from '$lib/components/avatar/index.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="container">
	<div class="header cyber-razor-bottom bg-dark">
		<div class="app-icon cyber-glitch-2">
			<Icon />
		</div>
		<h1 class="cyber-glitch-1 title">Recipe Manager</h1>

		<div class="whitespace-fill"></div>

		<div class="avatar-container">
			<Avatar />
		</div>

		<div class="user-details">
			<div class="username">harvey.manfredjensenden</div>
			<div class="site">My Special Kitchen</div>
		</div>
	</div>
	<div class="content">
		{@render children()}
	</div>
</div>

<style>
	.container {
		width: 100vw;
		height: 100vh;
	}
	.header {
		height: 46px;
		width: 100vw;
		display: flex;
		align-items: center;
		gap: 16px;
	}
	.app-icon {
		margin-left: 16px;
		width: 32px;
		height: 32px;
	}
	.title {
		color: white;
	}
	.whitespace-fill {
		flex-grow: 1;
	}
	.user-details {
		margin-right: 16px;
		color: white;
	}
	.username {
		font-weight: bold;
		font-size: 14px;
	}
	.site {
		font-size: 12px;
		opacity: 0.8;
		font-style: italic;
	}
	.avatar-container {
		margin-top: 10px;
	}
	.content {
		height: calc(100vh - (46px + 30px));
		width: 100vw;
		overflow: auto;
	}
</style>
