const BASE_URL = 'http://127.0.0.1:8090'; //import.meta.env.VITE_API_URL || ;
const API_PREFIX = '';

class RecipeAPIClient {
  constructor(baseUrl = BASE_URL) {
    this.baseUrl = baseUrl;
    this.apiPrefix = API_PREFIX;
  }

  /**
   * Make HTTP request
   * @param {string} endpoint - API endpoint path
   * @param {object} options - Request options
   * @returns {Promise<any>}
   */
  async request(endpoint, options = {}) {
    const url = `${this.baseUrl}${this.apiPrefix}${endpoint}`;

    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.detail || `HTTP ${response.status}: ${response.statusText}`);
      }

      // Return empty object for 204 No Content
      if (response.status === 204) {
        return null;
      }

      return await response.json();
    } catch (error) {
      console.error(`API Error [${endpoint}]:`, error);
      throw error;
    }
  }

  // ========================================================================
  // Recipe Endpoints
  // ========================================================================

  /**
   * Status
   * @returns {Promise<*>}
   */
  async getStatus() {
    return this.request('/status', {
      method: 'GET',
    });
  }

  /**
   * List all recipes
   * @returns {Promise<Array>}
   */
  async listRecipes() {
    return this.request('/recipes', {
      method: 'GET',
    });
  }

  /**
   * Search recipes by query string
   * @param {string} queryString - Search query
   * @param {number} page - Page number (default: 0)
   * @param {number} pageSize - Results per page (default: 100)
   * @returns {Promise<Array>}
   */
  async searchRecipes(queryString, page = 0, pageSize = 100) {
    const params = new URLSearchParams({
      query_string: queryString,
      page: page.toString(),
      page_size: pageSize.toString(),
    });

    return this.request(`/recipes/search?${params}`, {
      method: 'GET',
    });
  }

  /**
   * Get a single recipe by ID
   * @param {string} recipeId - Recipe ID
   * @returns {Promise<object>}
   */
  async getRecipe(recipeId) {
    return this.request(`/recipe/${recipeId}`, {
      method: 'GET',
    });
  }

  /**
   * Create a new recipe
   * @param {object} recipeData - Recipe data
   * @returns {Promise<object>}
   */
  async createRecipe(recipeData) {
    return this.request('/recipe', {
      method: 'POST',
      body: JSON.stringify(recipeData),
    });
  }

  /**
   * Update an existing recipe
   * @param {string} recipeId - Recipe ID
   * @param {object} recipeData - Updated recipe data
   * @returns {Promise<object>}
   */
  async updateRecipe(recipeId, recipeData) {
    return this.request(`/recipe/${recipeId}`, {
      method: 'POST',
      body: JSON.stringify(recipeData),
    });
  }

  /**
   * Archive a recipe
   * @param {string} recipeId - Recipe ID
   * @returns {Promise<object>}
   */
  async archiveRecipe(recipeId) {
    return this.request(`/recipe/${recipeId}/archive`, {
      method: 'POST',
    });
  }

  /**
   * Unarchive a recipe
   * @param {string} recipeId - Recipe ID
   * @returns {Promise<object>}
   */
  async unarchiveRecipe(recipeId) {
    return this.request(`/recipe/${recipeId}/unarchive`, {
      method: 'POST',
    });
  }
}

export default new RecipeAPIClient();
