<script>
  export let href = "";
  
  function navigate() {
    window.location.href = href;
  }
</script>

<button
  class="max-w-sm mx-auto bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
  on:click={navigate}
  disabled={!href}
>
  →  
</button>
