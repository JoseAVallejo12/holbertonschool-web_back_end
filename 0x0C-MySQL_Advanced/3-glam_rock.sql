-- script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT origin as band_name,
  style as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY split DESC;
