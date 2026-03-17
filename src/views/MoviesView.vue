<template>
  <div class="movies-container">
    <h1>Movies</h1>
    <div class="movies-grid">
      <div v-if="movies.length === 0" class="no-movies">
        No movies have been added yet.
      </div>
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" alt="Movie poster" class="movie-poster" />
        <div class="movie-details">
          <h3 class="movie-title">{{ movie.title }}</h3>
          <p class="movie-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const movies = ref([]);

const fetchMovies = () => {
  fetch('/api/v1/movies')
    .then(response => response.json())
    .then(data => {
      movies.value = data.movies;
      console.log('Movies loaded:', movies.value);
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
};

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.movie-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.movie-card:hover {
  transform: translateY(-5px);
}

.movie-poster {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-bottom: 1px solid #eee;
}

.movie-details {
  padding: 15px;
}

.movie-title {
  font-size: 18px;
  margin-bottom: 10px;
  color: #333;
}

.movie-description {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.no-movies {
  grid-column: 1 / -1;
  text-align: center;
  padding: 30px;
  color: #666;
  font-style: italic;
}
</style>