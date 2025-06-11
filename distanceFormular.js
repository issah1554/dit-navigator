function haversineDistanceInMeters(lat1, lon1, lat2, lon2) {
  const R = 6371e3; // Earth's radius in metres

  const toRad = (angle) => angle * (Math.PI / 180);

  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);

  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return R * c; // in metres
}

// Example usage:
// const lat1 = -6.815402490601152;
// const lon1 = 39.2795557694656;
// const lat2 = -6.82;
// const lon2 = 39.29;

// const distanceMeters = haversineDistanceInMeters(lat1, lon1, lat2, lon2);
// console.log(`Distance: ${distanceMeters.toFixed(2)} meters`);