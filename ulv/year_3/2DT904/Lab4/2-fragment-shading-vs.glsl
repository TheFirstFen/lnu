uniform mat4 mModel;
uniform mat4 mProjView;
in vec3 position;
in vec2 vertexUV;

out vec2 uv;
void main()
{
  gl_Position = mProjView * mModel * vec4(position, 1.0);
  uv = vertexUV;
}