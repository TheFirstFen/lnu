uniform float time;
in vec2 uv;

out vec4 fragColor;
void main() {
  vec3 yellow = vec3(1.0, 1.0, 0.0);
  vec3 blue = vec3(0.0, 0.0, 1.0);

  float a1 = step(0.3, uv.x);
  float a2 = step(0.5, uv.x);

  float b1 = step(0.4, uv.y);
  float b2 = step(0.6, uv.y);

  vec3 color = (a1-a2) * yellow + (b1-b2) * yellow + (1-a1+b2-b1) * blue + (a2 +b2-b1)* blue;
  
  //vec3 color = mix(yellow, blue, uv.x);

  //float a = step(0.2, uv.x);
  //float a2 = step(0.2, uv.y);
  //float total_mask = a * a2;
  //float s = smoothstep(0.2, 0.3, uv.x);
  // color = gl_FragCoord.x < 256. ? color : vec3(0);
  fragColor = vec4(color, 1.0);
}