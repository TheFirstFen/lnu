uniform mat4 mModel;
uniform mat4 mProjView;
in vec3 position;

out vec3 color;
void main()
{
  gl_Position = mProjView * mModel * vec4(position, 1.0);
  color = vec3(1.0, .6, 1.0);
}